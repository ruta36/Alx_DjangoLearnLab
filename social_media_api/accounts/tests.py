from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass')

    def test_follow_user(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(f'/api/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unfollow_user(self):
        self.client.login(username='user1', password='pass')
        self.client.post(f'/api/follow/{self.user2.id}/')
        response = self.client.post(f'/api/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

