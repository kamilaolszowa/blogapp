from rest_framework import serializers
from .models import Blogger, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'blogger']


class BloggerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Blogger
        fields = ['id', 'user_id']
