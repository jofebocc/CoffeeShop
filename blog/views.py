from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request, "blog/blog.html", {'post': post})


def category(request, category_id):
    cat = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': cat})
