from django.test import TestCase
from.models import Profile

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.Peris = Profile(name = 'Peris', profile_pic = 'image.jpeg', bio='Always conected to my instagram')
        self.Peris.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Peris, Profile))

    def test_save_method(self):
        self.Peris.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.Peris.save_profile()
        self.Peris.delete_profile.all()

        

