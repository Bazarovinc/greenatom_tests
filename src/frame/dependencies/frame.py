from fastapi import Depends, UploadFile, File, HTTPException, status
from typing import List
from src.frame.services.inbox import InboxService
from src.frame.utils.utils import check_or_create_directory, save_image, decode_image, delete_image
from src.frame.schemas.base.inbox import InboxSchema
from src.frame.schemas.response.inbox import InboxResponseSchema, FrameResponseSchema
from fastapi.responses import FileResponse
import uuid
from datetime import datetime


def save_images_and_record_into_db(
        images: List[UploadFile] = File(...),
        service: InboxService = Depends()
):
    if 15 < len(images):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='List of images should be in the range between 1 and 15'
                            )
    now = datetime.now().strftime('%Y%m%d')
    code = str(uuid.uuid4())
    check_or_create_directory()
    response = []
    for image in images:
        print(image.content_type)
        filename = str(uuid.uuid4()) + '.jpeg'
        check_or_create_directory(now, 'data')
        save_image('data/' + now + '/' + filename, image)
        response.append(
            InboxResponseSchema.from_orm(service.create(InboxSchema(filename=filename, code=code)))
        )
    return response


def get_images(code: str, service: InboxService = Depends()):
    response = []
    for obj in service.get_all(code):
        schema = InboxSchema.from_orm(obj)
        dir_name = schema.created_at.strftime('%Y%m%d')
        response.append(FrameResponseSchema(
            id=schema.id,
            code=schema.code,
            filename=schema.filename,
            created_at=schema.created_at,
            file=decode_image(f'data/{dir_name}/{schema.filename}')
        ))
    return response


def delete_images(code: str, service: InboxService = Depends()) -> str:
    for obj in service.get_all(code):
        schema = InboxSchema.from_orm(obj)
        dir_name = schema.created_at.strftime('%Y%m%d')
        delete_image(f'data/{dir_name}/{schema.filename}')
        service.delete(schema.id)
    return code
