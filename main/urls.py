from django.urls import path
from django.views.decorators.cache import cache_page
from main import views


urlpatterns = [
    # path('', cache_page(60)(views.IndexNews.as_view()), name="index"),
    path('', views.IndexNews.as_view(), name="index"),
    path('search/', views.Search.as_view(), name="search"),
    path('schedule/', views.schedule, name="schedule"),
    path('gallery/<slug:slug>/', views.PhotoGallery.as_view(), name="photo_gallery"),
    path('history/', views.history, name="history"),
    path('gallery/', views.Gallery.as_view(), name="gallery"),
    path('churches/<slug:slug>/', views.churches, name="churches"),
    path('typography/', views.typography, name="typography"),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_us, name="contact"),
    path('news/<slug:slug>/', cache_page(3600)(views.PostDetail.as_view()), name="post_detail"),
    # path('news/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('send_message/', views.send_message2, name="send_message"),
    path('old_index', views.old_index, name="old_index"),
]
