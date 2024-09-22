from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth.models import User

class LikeTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user2)

    def test_like_post(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(f'/api/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unlike_post(self):
        self.client.login(username='user1', password='pass')
        self.client.post(f'/api/posts/{self.post.id}/like/')
        response = self.client.post(f'/api/posts/{self.post.id}/unlike/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
