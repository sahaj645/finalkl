from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Story, Comment, UserProfile
from .serializers import StorySerializer, CommentSerializer, UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
