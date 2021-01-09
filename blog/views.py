from django.shortcuts import render
from .models import Blog

def blogs_view(request):
    context = {
        'page': 'blog',
        'blogs': Blog.objects.all()
    }

    return render(request, 'blog/blogs.html', context)

def blog_view(request, id):

    blog = Blog.objects.get(pk=id)

    context =  {
        'page': 'blog',
        'blog': blog
    }

    return render(request, 'blog/blog.html', context)