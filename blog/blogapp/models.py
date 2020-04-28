from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    news_text = models.TextField()
    posted = models.DateTimeField(auto_now_add=True, blank=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True, blank=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment = models.TextField()

class SubComment(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    pub_date = models.DateField()
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment = models.TextField()