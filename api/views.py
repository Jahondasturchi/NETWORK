from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer, PostSerializer
from app1.models import Profile, Post

class ProfileListApiVeiw(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PostListApiVeiw(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProfileRetry(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PostRetry(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer