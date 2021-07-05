from django.shortcuts import render, get_object_or_404
from .models import News, NewsImages, Schedule, Churches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


def index(request):
    news = News.objects.filter(is_published=True)
    churches = Churches.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "main/index.html", context={"news": news,
                                                       "page_obj": page_obj,
                                                       "churches": churches,
                                                       })


def schedule(request):
    schedule = Schedule.objects.first()
    return render(request, "main/schedule.html", {"schedule": schedule})


def churches(request, slug):
    churches = get_object_or_404(Churches, slug=slug)
    return render(request, "main/churches.html", {"churches": churches})


def history(request):
    history = Churches.objects.first()
    return render(request, "main/history.html", {"history": history})


def gallery(request):
    news = News.objects.filter(is_published=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 6)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "main/gallery.html", {"news": news,
                                                 "page_obj": page_obj})


def photo_gallery(request, id):
    photos = get_object_or_404(News, pk=id)

    return render(request, "main/photo_gallery.html", {"photos": photos})


def post_detail(request, id):
    post = get_object_or_404(News, pk=id)
    last_posts = News.objects.filter(is_published=True)[:3]
    return render(request, "main/post_detail.html", {"post": post,
                                                     "last_posts": last_posts,
                                                     })


def about_us(request):
    return render(request, "main/about-us.html")


def contact_us(request):
    return render(request, "main/contact-us.html")


def typography(request):
    return render(request, "main/typography.html")
