import uuid
from datetime import datetime
from typing import List

from fastapi import Depends, File, HTTPException, UploadFile, status

from src.frame.schemas.base.inbox import InboxSchema
from src.frame.schemas.response.inbox import (FrameResponseSchema,
                                              InboxResponseSchema)
from src.frame.services.inbox import InboxService
from src.frame.utils.utils import (check_or_create_directory, decode_image,
                                   delete_image, save_image)


def save_images_and_record_into_db(
        images: List[UploadFile] = File(...),
        service: InboxService = Depends()
):
    if 15 < len(images):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='List of images should be in the range between 1 and 15'
        )
    now = datetime.now().strftime('%Y%m%d')
    code = str(uuid.uuid4())
    check_or_create_directory()
    response = []
    for image in images:
        filename = str(uuid.uuid4()) + '.jpeg'
        check_or_create_directory(now, 'data')
        save_image('data/' + now + '/' + filename, image)
        response.append(
            InboxResponseSchema.from_orm(service.create(InboxSchema(filename=filename, code=code)))
        )
    return response


def get_images(code: str, service: InboxService = Depends()):
    response = []
    if images := service.get_all(code):
        for obj in images:
            schema = InboxSchema.from_orm(obj)
            dir_name = schema.created_at.strftime('%Y%m%d')
            response.append(FrameResponseSchema(
                id=schema.id,
                code=schema.code,
                filename=schema.filename,
                created_at=schema.created_at,
                file=decode_image(f'data/{dir_name}/{schema.filename}')
            ))
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No images with code {code}'
        )
    return response


def delete_images(code: str, service: InboxService = Depends()) -> str:
    if images := service.get_all(code):
        for obj in images:
            schema = InboxSchema.from_orm(obj)
            dir_name = schema.created_at.strftime('%Y%m%d')
            delete_image(f'data/{dir_name}/{schema.filename}')
            service.delete(schema.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No images with code {code}'
        )
    return code
