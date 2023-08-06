from rest_framework import serializers
from app1.models import Profile, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'follows']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user', 'body', 'created_at']

