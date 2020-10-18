from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.
class Profile(models.Model):
    name =  models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to = 'images/',default = '')
    bio = models.TextField()

    def save_profile(self):
        self.save

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

    
class  Post(models.Model):
    image = models.ImageField(blank=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    post = HTMLField()
    caption = models.CharField(max_length=300) 
    post = models.TextField()


