from django.shortcuts import render, get_object_or_404
from .models import News, Schedule, Churches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


class IndexNews(ListView):
    model = News
    template_name = "main/index.html"
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(is_published=True)

    def get_churches(self):
        return Churches.objects.all()


class PostDetail(DetailView):
    model = News
    template_name = "main/post_detail.html"
    context_object_name = 'post'

    def get_queryset(self):
        return News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Gallery(ListView):
    model = News
    paginate_by = 20
    template_name = "main/gallery.html"
    context_object_name = "post"

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class PhotoGallery(DetailView):
    model = News
    template_name = "main/photo_gallery.html"
    context_object_name = "photos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    paginate_by = 3
    template_name = "main/index.html"

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


# def index(request):
#     news = News.objects.filter(is_published=True)
#     churches = Churches.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(news, 3)
#     try:
#         page_obj = paginator.page(page)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.num_pages)
#     return render(request, "main/index.html", context={"news": news,
#                                                        "page_obj": page_obj,
#                                                        "churches": churches,
#                                                        })


def schedule(request):
    schedule = Schedule.objects.first()
    return render(request, "main/schedule.html", {"schedule": schedule})


def churches(request, slug):
    churches = get_object_or_404(Churches, slug=slug)
    return render(request, "main/churches.html", {"churches": churches})


def history(request):
    history = Churches.objects.first()
    return render(request, "main/history.html", {"history": history})



# def gallery(request):
#     news = News.objects.filter(is_published=True)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(news, 6)
#     try:
#         page_obj = paginator.page(page)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.num_pages)
#     return render(request, "main/gallery.html", {"news": news,
#                                                  "page_obj": page_obj})
#
#
# def photo_gallery(request, id):
#     photos = get_object_or_404(News, pk=id)
#
#     return render(request, "main/photo_gallery.html", {"photos": photos})


# def post_detail(request, id):
#     post = get_object_or_404(News, pk=id)
#     last_posts = News.objects.filter(is_published=True)[:3]
#     return render(request, "main/post_detail.html", {"post": post,
#                                                      "last_posts": last_posts,
#                                                      })


def about_us(request):
    return render(request, "main/about-us.html")


def contact_us(request):
    return render(request, "main/contact-us.html")


def typography(request):
    return render(request, "main/typography.html")
