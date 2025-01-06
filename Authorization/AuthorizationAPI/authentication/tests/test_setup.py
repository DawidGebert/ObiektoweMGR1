from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data={
            'email':"email@gamil.com",
            'username':"email",
            'password':"email@gamil.com"
        }


    def tearDown(self):
        return super().tearDown()
    
    