from fastapi import APIRouter
from src.frame.api import frame

router = APIRouter()

router.include_router(frame.router, tags=['frame'], prefix='/frame')
