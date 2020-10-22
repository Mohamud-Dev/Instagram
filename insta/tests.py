from django.test import TestCase
from.models import Profile

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.Peris = Profile(name = 'Peris', profile_pic = 'image.jpg', bio='Always conected to my instagram')
        self.Peris.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Peris, Profile))

    def test_save_method(self):
        self.Peris.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.profile_pic.delete_profile_pic()
        Profile = Profile.objects.all()
        self.assertTrue(len(Locations)==2) 



class PostTestCase(TestCase):

    def setUp(self):
        self.hiking = Profile(image= 'image.jpg', title = 'hiking', user='User')
        self.hiking.save()


    def tearDown(self):
        Post.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.hiking, Post))


    def  test_save_method(self):
        self.Peris.save_post()
        tittle = Post.objects.all()
