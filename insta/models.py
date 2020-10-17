from django.db import models

# Create your models here.
class Profile(models.Model):
    name =  models.CharField(max_length = 30)
    profile_pic = models.ImageField(upload_to = 'images/',default = '')
    bio = models.TextField()

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()
# class Comments(models.Model):
#     comment = models.CharField(max_length = 500)
#     user = models.ForeignKey()









