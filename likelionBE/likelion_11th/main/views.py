from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone



# Create your views here.

def create(request) :

    new_post = Post()

    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.fanname = request.POST['fanname']
    new_post.hashtag = request.POST['hashtag']

    new_post.save()

    return redirect('detail', new_post.id)

def new(request):
    return render(request, 'main/new.html')

def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def secondpage(request):
    return render(request, 'main/secondpage.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})