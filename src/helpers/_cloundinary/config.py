from django.conf import settings
import cloudinary
CLOUDINARY_CLOUD_NAME = settings.CLOUDINARY_CLOUD_NAME
CLOUDINARY_CLOUND_API_KEY = settings.CLOUDINARY_CLOUND_API_KEY
CLOUDINARY_CLOUND_API_SECRET = settings.CLOUDINARY_CLOUND_API_SECRET
def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_CLOUND_API_KEY, 
        api_secret = CLOUDINARY_CLOUND_API_SECRET,
        secure=True # make sure it is https instead of http 
    )

