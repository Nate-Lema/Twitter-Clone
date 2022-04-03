from hashlib import new
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

from cloudinary.forms import cl_init_js_callbacks
from cloudinary.forms import cl_init_js_callbacks
from django.urls import reverse_lazy, reverse

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json)
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request,'posts.html',{'posts':posts})

def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def update(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm
        return render(request,'update.html',{'post':post,'form':form})

def like(request,post_id):
    post = Post.objects.get(id=post_id)
    newlikecount = post.like_count+1
    post.like_count = int(newlikecount)
    post.save()
    return HttpResponseRedirect('/')


