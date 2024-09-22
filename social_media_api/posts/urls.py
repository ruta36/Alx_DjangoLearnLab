from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),
    path('<int:pk>/like/', LikePost.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePost.as_view(), name='unlike_post'),
    path('', NotificationListView.as_view(), name='notification_list'),
]




