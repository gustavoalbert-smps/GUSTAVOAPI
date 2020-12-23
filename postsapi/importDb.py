import json
from DevPosts.models import Profile, Post, Comment

jsons = open('db.json', 'r')
data = json.loads(jsons.read())

for i in data['users']:
    pro_id = i['id']
    profile_name = i['name']
    profile_email = i['email']
    profile1 = Profile(profile_id = pro_id, name = profile_name, email = profile_email)
    profile1.save()

for i in data['posts']:
    pro_id = Profile.objects.get(profile_id = i['userId'])
    post_ident = i['id']
    post_title = i['title']
    post_body = i['body']
    post1 = Post(post_id = post_ident, title = post_title, body = post_body, userId = pro_id)
    post1.save()


for i in data['comments']:
    post_id = Post.objects.get(post_id = i['postId'])
    com_id = i['id']
    comment_name = i['name']
    comment_email = i['email']
    comment_body = i['body']
    comment1 = Comment(comment_id = com_id, name = comment_name, email = comment_email, body = comment_body, postId = post_id)
    comment1.save()