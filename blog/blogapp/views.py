from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from . import models
# Create your views here.

def blog(request):
    posts = models.Post.objects.all()
    print(dir(request))
    return render(request, 'blog/main.html', {'posts':posts})

def post(request, id):
    post = models.Post.objects.get(id=id)
    comments = models.Comment.objects.filter(post_id=id)
    if request.method == "POST":
        user_id = int(request.user.id)
        user = User.objects.get(id=user_id)
        comment = request.POST['comment']
        models.Comment.objects.create(post_id=post, user_id=user, comment=comment)
    
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/post.html', context)

def check(request):
    if request.method == "POST":
        user_id = int(request.user.id)
        user = User.objects.get(id=user_id)
        data = request.POST
        title = data['title']
        news_text = data['text']
        models.Post.objects.create(user_id=user, title=title, news_text=news_text)
        return redirect(blog)

    return render(request, 'blog/add.html', {})


    