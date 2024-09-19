from django.contrib import admin
from .models import Course
from django.utils.html import format_html
from cloudinary import CloudinaryImage
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display =['title','status','access']
    list_filter = ['status','access']
    fields = ['title','description','status','image','access','display_image']
    readonly_fields = ['display_image']
    def display_image(self,obj,*args,**kwargs):
        image_url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
        cloudinary_html2 = obj.image.image(width=200) # another way to do it 
        

        return format_html(cloudinary_html)
    
    display_image.short_description = 'current image'
