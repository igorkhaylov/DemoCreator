from django.shortcuts import render, get_object_or_404
from .models import News, NewsImages, Schedule, Churches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


def index(request):
    news = News.objects.filter(is_published=True)
    churches = Churches.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(news, 6)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    # paginator = Paginator(news, 2) # Show 25 contacts per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, "main/index.html", context={"news": news,
                                                       "page_obj": page_obj,
                                                       "churches": churches,
                                                       })


def schedule(request):
    schedule = Schedule.objects.first()
    return render(request, "main/schedule.html", {"schedule": schedule})


def churches(request, slug):
    churches = get_object_or_404(Churches, slug=slug)
    # churches = Churches.objects.all(slug=slug)
    return render(request, "main/churches.html", {"churches": churches})


def history(request):
    history = Churches.objects.first()
    return render(request, "main/history.html", {"history": history})


def gallery(request):
    return render(request, "main/gallery.html")


def post_detail(request, id):
    # post = News.objects.get(pk=id)
    post = get_object_or_404(News, pk=id)
    last_posts = News.objects.filter(is_published=True)[:3]
    # images = NewsImages.objects.filter(post_id=id)
    return render(request, "main/post_detail.html", {"post": post,
                                                     "last_posts": last_posts,
                                                     })


def about_us(request):
    return render(request, "main/about-us.html")


def contact_us(request):
    return render(request, "main/contact-us.html")


def typography(request):
    return render(request, "main/typography.html")
