from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blog = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blogs': blog})


def blogpostdetail(request, blog_id):
    blogpost = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detailblog.html', {'detailblog': blogpost})
