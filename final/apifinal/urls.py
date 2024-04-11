from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import StoryViewSet, CommentViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
