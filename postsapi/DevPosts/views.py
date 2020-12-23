from django.shortcuts import render

from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from DevPosts.models import Profile, Post, Comment
from DevPosts.serializers import ProfileSerializer, PostSerializer, CommentSerializer, ProfilePostSerializer, PostCommentCounterSerializer

# Create your views here.

#profile
class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profiles-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profiles-detail'

class ProfilePostList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profiles-posts'

class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profiles-posts'

#post
class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-detail'

class PostCommentsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-comments'

class PostCommentDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-comments'

#comment
class CommentsList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comments-list'

    def get_queryset(self):
        queryset = Comment.objects.filter(postId=self.kwargs.get('postId'))
        return queryset

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comments-detail'

#totalPostComments
class PostCommentCounter(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(profile_id=kwargs['pk'])
        total_posts = profile.count_posts()
        total_comments = profile.count_comments()
        data = {'pk':profile.profile_id, 'name': profile.name, 'posts': total_posts, 'comments': total_comments}
        serializer = PostCommentCounterSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    name = 'posts-comments-counter'

#ROOT
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profiles': reverse(ProfilesList.name, request=request),
            'profiles-posts': reverse(ProfilePostList.name, request=request),
            'posts-comments': reverse(PostCommentsList.name, request=request),
        })