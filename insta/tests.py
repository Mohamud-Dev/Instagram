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
        self.Peris.name()
        name = Profile.objects.all()

        

