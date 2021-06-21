from django.shortcuts import render
from .models import News, NewsImages
from django.http import HttpResponse


def index(request):
    news = News.objects.filter(is_published=True)
    return render(request, "main/index.html", context={"news": news})


def post_detail(request, id):
    post = News.objects.get(pk=id)
    # images = NewsImages.objects.filter(post_id=id)
    return render(request, "main/post_detail.html", {"post": post})


def about_us(request):
    return render(request, "main/about-us.html")


def contact_us(request):
    return render(request, "main/contact-us.html")


def typography(request):
    return render(request, "main/typography.html")
