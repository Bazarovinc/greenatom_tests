from fastapi import FastAPI
from src.frame.api.router import router as frame_router


def get_application() -> FastAPI:
    application = FastAPI(title="app", debug=True)

    application.include_router(frame_router, prefix="/api")

    return application


app = get_application()
