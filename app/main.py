from fastapi import FastAPI
from app.core.config import DEBUG, VERSION, DESCRIPTION, PROJECT_NAME


def build_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, description=DESCRIPTION, version=VERSION)
    return application


template_api = build_application()


@template_api.get("/")
async def root():
    return {"message": "Hello World"}
