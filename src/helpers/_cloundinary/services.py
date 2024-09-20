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

video_html = """
<video controls autopaly >
<source  src="{video_url}"/>
</video>

""".strip()
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
          return video_html.format(video_url=url).strip()
          
   # unpacking te image dict

    return url


