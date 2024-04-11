from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import StoryViewSet, CommentViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'comments', CommentViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# Define additional URL patterns for subsections of stories
urlpatterns += [
    path('stories/top/', StoryViewSet.as_view({'get': 'top'}), name='story-top'),
    path('stories/new/', StoryViewSet.as_view({'get': 'new'}), name='story-new'),
    path('stories/best/', StoryViewSet.as_view({'get': 'best'}), name='story-best'),
]
