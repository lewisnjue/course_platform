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
    


