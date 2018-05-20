from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Blog,Category,Tag
# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def  detail(request,blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    query_set = Blog.objects.order_by('-created_at').filter(category=category)
    return render(request, 'blog/category_detail.html', {'category':category,'query_set':query_set}) # in this template, you will have access to category and posts under that category by (category.post_set).

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    query_set = Blog.objects.order_by('-created_at').filter(tag=tag)
    return render(request, 'blog/tag_detail.html', {'tag':tag,'query_set':query_set})