from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog

def blogs_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page') if request.GET.get('page') else 1

    page = paginator.get_page(page_number)

    context = {
        'page': 'blog',
        'page_num': page.start_index(),
        'blogs': page,
        'pages': paginator.num_pages,
        'has_next': page.has_next(),
        'has_prev': page.has_previous()
    }

    return render(request, 'blog/blogs.html', context)

def blog_view(request, id):

    blog = Blog.objects.get(pk=id)

    context =  {
        'page': 'blog',
        'blog': blog
    }

    return render(request, 'blog/blog.html', context)