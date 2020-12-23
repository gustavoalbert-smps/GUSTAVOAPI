from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)

    def count_posts(self):
        total_posts = Post.objects.filter(userId=self).count()
        return total_posts

    def count_comments(self):
        total_comments = Comment.objects.filter(postId__userId=self).count()
        return total_comments

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    userId = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.CharField(max_length=500)
    postId = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)