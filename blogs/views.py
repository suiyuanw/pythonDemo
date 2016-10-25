from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    query = {
        'published_date__lte': timezone.now(),
    }
    posts = Post.objects.filter(**query).order_by('published_date')
    result = []
    for post in posts:
        result.append(post.dict())
    return render(request, 'blogs/post_list.html', {
        'posts': result,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {
        'post': post.dict(),
    })
