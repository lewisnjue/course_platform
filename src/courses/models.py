from django.db import models

# Create your models here.

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
    image = models.ImageField(upload_to=handle_upload,blank=True,null=True) 
    access = models.CharField(max_length=20,choices=AccessReguirments.choices)
    status = models.CharField(max_length=10,choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT)
    @property
    def is_published(self):
        return self.status == 'pub'
    


