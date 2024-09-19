
import cloudinary
from decouple import config # the small letter config 

CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_CLOUND_API_KEY = config("CLOUDINARY_CLOUND_API_KEY")
CLOUDINARY_CLOUND_API_SECRET = config("CLOUDINARY_CLOUND_API_SECRET")
def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_CLOUND_API_KEY, 
        api_secret = CLOUDINARY_CLOUND_API_SECRET,
        secure=True
    )

