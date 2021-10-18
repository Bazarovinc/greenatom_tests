from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException, Response
from typing import List
from src.frame.schemas.response.inbox import InboxResponseSchema, FrameResponseSchema
from src.frame.dependencies.frame import save_images_and_record_into_db, get_images, delete_images
from fastapi.responses import FileResponse

router = APIRouter()


@router.put('', status_code=status.HTTP_201_CREATED, response_model=List[InboxResponseSchema])
def put_images_view(images=Depends(save_images_and_record_into_db)) -> List[InboxResponseSchema]:
    return images


@router.get('/{code}', response_model=List[FrameResponseSchema])
def get_images_by_code_view(images=Depends(get_images)) -> List[FrameResponseSchema]:
    return images


@router.delete('/{code}', status_code=status.HTTP_204_NO_CONTENT)
def delete_images_by_code_view(code=Depends(delete_images)):
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
        content=f'All images with code {code} had been successefully deleted.'
    )
