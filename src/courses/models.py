from typing import Iterable
from django.db import models
import helpers
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
import uuid
# Create your models here.
helpers.cloudinary_init() # that is all you will need to do 



class AccessReguirments(models.TextChoices):
    ANYONE = "any","anyone"
    EMAIL_REQUIRED = "email_required"," email required"




class PublishStatus(models.TextChoices):
    PUBLISHED = "pub","published"
    DRAFT = "draft","draft"
    COMING_SOON = 'soon',"coming soon"


def handle_upload(intance,filename):
    return f"{filename}"

def get_public_id(instance,*args,**kwargs):
    title = instance.title
    unique_id = str(uuid.uuid4()).replace("-","")
    if not title:
        
        return unique_id
    slug = slugify(title)
    unique_id_short = unique_id[:5]
    return f"{slug}--{unique_id}"




def get_public_id_prefix(instance,*args,**kwargs):
    if hasattr(instance,'path'):
        path = instance.path
        if path.startswith("/"):
            path = path[1:]
            if path.endswith('/'):
                path = path[:-1]
        return path
    
    public_id = instance.public_id
    if not public_id:
        return "courses"
    return f"courses/{public_id}"


def get_display_name(instance,*args,**kwargs):
    if hasattr(instance,'title'):
        return instance.title
    if hasattr(instance,'get_display_name'):
        return instance.get_display_name
    models_class = instance.__class__
    model_name = models_class.__name__
    return  f"{model_name} upload"

class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    #image = models.ImageField(upload_to=handle_upload,blank=True,null=True) 
    image = CloudinaryField('image',null=True, public_id_prefix=get_public_id_prefix,display_name=get_display_name,tags=["course","thumbnail"])
    access = models.CharField(max_length=20,choices=AccessReguirments.choices,
                              default=AccessReguirments.EMAIL_REQUIRED)
    status = models.CharField(max_length=10,choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT)
    public_id = models.CharField(max_length=130,null=True,blank=True)
    @property
    def path(self):
        return f"/courses/{self.public_id}"
    def save(self,*args,**kwargs):
        if self.public_id == '' or self.public_id is None:
            self.public_id = get_public_id(self)
        super().save(*args,**kwargs)

    def get_display_name(self):

        return f"{self.title} - course"
    


    @property
    def is_published(self):
        return self.status == 'pub'
    @property
    def image_admin(self):
        if not self.image:
            return ""
        image_options ={
            "width":200
        }
        url = self.image.build_url(**image_options) # unpacking te image dict

        return url
    def get_image_detail(self,as_html=False,width=750):
        if not self.image:
            return ""
        image_options ={
            "width":width
        }
        if as_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options) # unpacking te image dict

        return url
        def get_image_thumbnail(self,as_html=False,width=500):
            if not self.image:
                return ""
            image_options ={
                "width":width
            }
            if as_html:
                return self.image.image(**image_options)
            url = self.image.build_url(**image_options) # unpacking te image dict

            return url

    
"""

 in python the @property decorator is used to 
define attributes taht are computed dynamically 
rather than stored as fixed values 
it provides a way to encapsulate teh logic for calculating the attributes 
value, making the cass interface more readable and mantanable 
SETTER METHOD : you can optinally define a setter method using the 
@property.setter decorator . this allows you to mdofy the attributes value 
potentailly performing validation or calculations before updateing the underlying 
data 
DELETER METHOD : simlilarly you can define a deleter method using the 
@property.deleter decorator to remote the attriubtes 

 """


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    public_id = models.CharField(max_length=130,null=True,blank=True)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    thumbnail = CloudinaryField('image',null=True,blank=True,public_id_prefix=get_public_id_prefix,display_name=get_display_name,tags=['thumbnail','lesson'])
    video = CloudinaryField('video',resource_type='video',null=True,blank=True,public_id_prefix=get_public_id_prefix,display_name=get_display_name,tags=['video','thumbnail','lesson'])
    can_preview = models.BooleanField(default=False,help_text="if user dont have access to this course can they see this ")
    order = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default= PublishStatus.PUBLISHED
    )
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['order','-updated']

    def save(self,*args,**kwargs):
        if self.public_id == '' or self.public_id is None:
            self.public_id = get_public_id(self)
        super().save(*args,**kwargs)
    @property
    def path(self):
        course_path = self.course.path
        if course_path.endswith('/'):
            course_path = course_path[:-1]


        return f"{course_path}/lessons/{self.public_id}"
    def get_display_name(self):
        return f"{self.title} - {self.course.get_display_name()}"
    

