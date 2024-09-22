from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

class PostTests(APITestCase):
    def test_create_post(self):
        url = reverse('post-list')
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Log in and test again...
