from django.urls import path
from DevPosts import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('profiles/', views.ProfilesList.as_view(), name=views.ProfilesList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('profile-posts/', views.ProfilePostList.as_view(), name=views.ProfilePostList.name),
    path('profile-posts/<int:pk>/', views.ProfilePostDetail.as_view(), name=views.ProfilePostDetail.name),
    path('posts-comments/', views.PostCommentsList.as_view(), name=views.PostCommentsList.name),
    path('posts-comments/<int:pk>/', views.PostCommentDetail.as_view(), name=views.PostCommentDetail.name),
    path('posts/<int:postId>/comments/', views.CommentsList.as_view(), name=views.CommentsList.name),
    path('posts/<int:postId>/comments/<int:pk>/', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    path('postscommentscounter/<int:pk>/', views.PostCommentCounter.as_view(), name=views.PostCommentCounter.name),
]