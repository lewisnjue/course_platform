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
