from django.contrib import admin
from .models import Course,Lesson
from django.utils.html import format_html
from cloudinary import CloudinaryImage
# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ['updated','public_id']
    extra = 0
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
