import os
from fastapi import UploadFile
import cloudinary
import cloudinary.uploader
import config
import os

cloudinary.config( 
  cloud_name = os.environ.get('cloudname'), 
  api_key = os.environ.get('api_key'), 
  api_secret = os.environ.get('api_secret') 
)

def upload_image(image_binary: UploadFile) -> dict:
    result = cloudinary.uploader.upload(image_binary.file, public_id=image_binary.filename, folder="image-uploads", overwrite=True, resource_type="image")
    return result