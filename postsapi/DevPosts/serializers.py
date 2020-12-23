from rest_framework import serializers
from DevPosts.models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_id','name', 'email')

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'email', 'posts')

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    
    class Meta:
        model = Post
        fields = ('title', 'body', 'userId', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'postId')

class PostCommentCounterSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField()
    posts = serializers.IntegerField()
    comments = serializers.IntegerField()