from django.contrib import admin
from .models import Course,Lesson
from django.utils.html import format_html # for enabling me to return html in my admin page 
import helpers
from cloudinary import CloudinaryImage # for me to render image stored in cloundinary and alter its size 
# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ['updated','public_id','display_image','display_video']
    extra = 0

    def display_image(self,obj,*args,**kwargs):
        image_url = helpers.get_cloudinary_img_object(obj,width=200,field_name='thumbnail')
        return format_html(f"<img src={image_url} />" )
    def display_video(self,obj,*args,**kwargs):
        image_url = helpers.get_cloudinary_video_object(obj,width=500,field_name='video',as_html=True)
        
        return format_html(f"{image_url}" )
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines= [LessonInline]
    list_display =['title','status','access']
    list_filter = ['status','access']
    fields = ['public_id','title','description','status','image','access','display_image']
    readonly_fields = ['display_image','public_id']
    def display_image(self,obj,*args,**kwargs):
        image_url = obj.image_admin
        cloudinary_id = str(obj.image)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
        cloudinary_html2 = obj.image.image(width=200) # another way to do it 
        

        return format_html(f"<img src={image_url} />" )
    
    display_image.short_description = 'current image'
