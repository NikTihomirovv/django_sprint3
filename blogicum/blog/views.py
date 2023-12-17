from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
import datetime


def index(request):
    post_list = Post.objects.select_related(
        'category',
        'author',
        'location').filter(
            pub_date__lte=datetime.datetime.now(),
            is_published=True,
            category__is_published=True)[:5]

    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post_list = get_object_or_404(Post.objects.select_related(
        'category',
        'location').filter(
            category__is_published=True,
            is_published=True,
            pub_date__lte=datetime.datetime.now(),
            pk=id),
    )

    context = {
        'post': post_list
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    post_list = get_object_or_404(Category,
                                  slug=category_slug)
    post_list = category.categories.filter(
        is_published=True,
        pub_date__lte=datetime.datetime.now())

    context = {
        'post_list': post_list,
        'category': category
    }
    return render(request, 'blog/category.html', context)
