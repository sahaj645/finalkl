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

    def top(self, request):
        top_stories = self.get_queryset().order_by('-upvotes')[:10]  # Assuming upvotes field exists
        serializer = self.get_serializer(top_stories, many=True)
        return Response(serializer.data)

    def new(self, request):
        new_stories = self.get_queryset().order_by('-created_at')[:10]  # Assuming created_at field exists
        serializer = self.get_serializer(new_stories, many=True)
        return Response(serializer.data)

    def best(self, request):
        best_stories = self.get_queryset().order_by('-rating')[:10]  # Assuming rating field exists
        serializer = self.get_serializer(best_stories, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
