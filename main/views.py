from django.shortcuts import render, get_object_or_404
from .models import News, Schedule, Churches, MainPagePicture, NewsImages
from django.db.models import F
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.core.cache import cache


class IndexNews(ListView):
    model = News
    template_name = "main/index.html"
    paginate_by = 6

    def get_queryset(self):
        main_news = cache.get("main_news")
        if not main_news:
            main_news = News.objects.filter(is_published=True)
            cache.set("main_news", main_news, 300)
        return main_news

    def get_churches(self):
        churches = cache.get("churches")
        if not churches:
            churches = Churches.objects.all()
            cache.set("churches", churches, 3600)
        return churches

    def get_main_pictures(self):
        main_picture = cache.get("main_picture")
        if not main_picture:
            main_picture = MainPagePicture.objects.all()
            cache.set("main_picture", main_picture, 3600)
        return main_picture


class PostDetail(DetailView):
    model = News
    template_name = "main/post_detail.html"
    context_object_name = 'post'

    def get_queryset(self):
        news_details = cache.get("news_details")
        if not news_details:
            news_details = News.objects.all()
            cache.set("news_details", news_details, 3600)
        return news_details
        # return News.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     self.object.views = F('views') + 1
    #     self.object.save()
    #     self.object.refresh_from_db()
    #     return context


class Gallery(ListView):
    model = News
    paginate_by = 20
    template_name = "main/gallery.html"
    context_object_name = "post"

    def get_queryset(self):
        # images = cache.get("images_cache")
        # if not images:
        #     images = NewsImages.objects.all()
        #     cache.set("images_cache", images, 10)
        l = []
        images = NewsImages.objects.all()
        for image in images:
            if image.post_id not in l:
                l.append(image.post_id)
        return News.objects.filter(id__in=l)


class PhotoGallery(DetailView):
    model = News
    template_name = "main/photo_gallery.html"
    context_object_name = "photos"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     self.object.views = F('views') + 1
    #     self.object.save()
    #     self.object.refresh_from_db()
    #     return context


class Search(ListView):
    paginate_by = 6
    template_name = "main/index.html"

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

    def get_churches(self):
        churches = cache.get("churches")
        if not churches:
            churches = Churches.objects.all()
            cache.set("churches", churches, 3600)
        return churches

    def get_main_pictures(self):
        main_picture = cache.get("main_picture")
        if not main_picture:
            main_picture = MainPagePicture.objects.all()
            cache.set("main_picture", main_picture, 3600)
        return main_picture


def schedule(request):
    schedule = cache.get("schedule_cache")
    if not schedule:
        schedule = Schedule.objects.first()
        cache.set("schedule_cache", schedule, 3600)
    return render(request, "main/schedule.html", {"schedule": schedule})


def churches(request, slug):
    churches = get_object_or_404(Churches, slug=slug)
    return render(request, "main/churches.html", {"churches": churches})


def history(request):
    history = cache.get("history_cache")
    if not history:
        history = Churches.objects.first()
        cache.set("history_cache", history, 3600)
    # history = Churches.objects.first()
    return render(request, "main/history.html", {"history": history})


def about_us(request):
    return render(request, "main/about-us.html")


def contact_us(request):
    # print("This is contact us page")
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone_number = request.POST["phone"]
        text = request.POST["message"]
        mes = "\tИмя отправителя: \n" + name + \
              "\n\n\tE-mail отправителя: \n" + email + \
              "\n\n\tНомер телефона: \n" + phone_number + \
              "\n\n\tСообщение: \n" + text

        mail = send_mail('Hram-Alekseevskii', mes, 'totpravka@gmail.com',
                         ['igorkhaylov@yandex.com', ], fail_silently=False, )
        if mail:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка отправки сообщения")

        print(request)
        # return HttpResponseRedirect()

        return render(request, "main/contact-us.html")

    return render(request, "main/contact-us.html")


def typography(request):
    return render(request, "main/typography.html")


def old_index(request):
    return render(request, "main/old_index.html")


def send_message2(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone_number = request.POST["phone"]
        text = request.POST["message"]
        mes = "\tИмя отправителя: \n" + name + \
              "\n\n\tE-mail отправителя: \n" + email + \
              "\n\n\tНомер телефона: \n" + phone_number + \
              "\n\n\tСообщение: \n" + text

        mail = send_mail('Hram-Alekseevskii', mes, 'totpravka@gmail.com',
                         ['igorkhaylov@yandex.com', ], fail_silently=False, )
        if mail:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка отправки сообщения")

        # print(request)
        # return HttpResponseRedirect()

        # return render(request, "main/contact-us.html")
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")


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
