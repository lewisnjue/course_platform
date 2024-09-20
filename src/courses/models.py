from django.db import models
import helpers
from cloudinary.models import CloudinaryField

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


class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    #image = models.ImageField(upload_to=handle_upload,blank=True,null=True) 
    image = CloudinaryField('image',null=True)
    access = models.CharField(max_length=20,choices=AccessReguirments.choices,
                              default=AccessReguirments.EMAIL_REQUIRED)
    status = models.CharField(max_length=10,choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT)
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
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    thumbnail = CloudinaryField('image',null=True,blank=True)
    video = CloudinaryField('video',resource_type='video',null=True,blank=True)
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
