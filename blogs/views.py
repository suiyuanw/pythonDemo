#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wufd at 2016/10/25

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    query = {
        'published_date__lte': timezone.now(),
    }
    posts = Post.objects.filter(**query).order_by('published_date')
    result = []
    for post in posts:
        result.append(post.to_dict())
    return render(request, 'blogs/post_list.html', {
        'posts': result,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {
        'post': post.to_dict(),
    })


def post_new(request):
    if request.method == 'post':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogs.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogs/post_edit.html', {
        'form': form,
    })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogs.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_edit.html', {
        'form': form,
    })
