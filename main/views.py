from django.shortcuts import render
from .models import News, NewsImages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


# class Index(ListView):
#     model = News
#     template_name = "main/index.html"
#     context_objects_name = 'news'
#     paginate_by = 2
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Classic Blog Design"
#         return context
def index(request):
    news = News.objects.filter(is_published=True)
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
                                                       })


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
