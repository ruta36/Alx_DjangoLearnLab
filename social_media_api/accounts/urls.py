from django.urls import path
from .views import RegisterView, LoginView, FollowUser, UnfollowUser, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
     path('users/', UserListView.as_view(), name='user_list'),
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow_user'),
]
