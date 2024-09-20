from    django.template.loader import get_template
from django.conf import settings
def get_cloudinary_img_object(instance,field_name="image",as_html=False,width=200):
          
    if not hasattr(instance,field_name):
            return ""
    img_object = getattr(instance,field_name)
    if not img_object:
          return ""
    
    image_options ={
            "width":width
    }
    if as_html:
          return img_object.image(**image_options)
    url = img_object.build_url(**image_options) # unpacking te image dict

    return url

video_html = ...

def get_cloudinary_video_object(instance,field_name="video",as_html=False,width=None,sign_url=False,height=None,fetch_format='auto',quality='auto',controls=True,autoplay=True):
          
    if not hasattr(instance,field_name):
            return ""
    video_object = getattr(instance,field_name)
    if not video_object:
          return ""
    
    video_options ={
            "sign_url":sign_url,
            "fetch_format":fetch_format,
            "quality":quality,
            "controls":controls,
            "autoplay":autoplay
    }
    if width:
          video_options['width'] = width
    if height:
          video_options['height'] = height
    if height and width:
          video_options['crop'] = 'limit'
    url = video_object.build_url(**video_options)
    if as_html:
          template_name = "videos/snippets/embend.html"
          tmpl = get_template(template_name=template_name)
          cloud_name = settings.CLOUDINARY_CLOUD_NAME
          _html = tmpl.render({'video_url':url,'cloud_name':cloud_name})
          return _html
          
   # unpacking te image dict

    return url


