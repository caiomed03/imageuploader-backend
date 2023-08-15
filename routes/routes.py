from fastapi import APIRouter, UploadFile
from services import image_service

router = APIRouter(
    prefix='/api',
)

@router.post('/upload')
async def upload_image(image: UploadFile):
    return image_service.upload_image(image)
