from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='new_post/', blank = 'true')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)

    def save_profile(self):
        self.save

    def delete_profile(self):
        self.delete()

   
    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    image = models.ImageField(upload_to='new_post/', blank=True ,default = 'default.jpg')
    title = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    caption = models.TextField(max_length=300)
    # likes = models.IntegerField(User, default=None, blank =True)

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all.count()



LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Likes',max_length=10)
    
    def __str__(self):
        return str(self.post)


 
