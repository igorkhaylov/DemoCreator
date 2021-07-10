from django.urls import path
from main import views


urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.IndexNews.as_view(), name="index"),
    path('search/', views.Search.as_view(), name="search"),
    path('schedule/', views.schedule, name="schedule"),
    # path('photo_gallery/<int:id>/',views.photo_gallery, name="photo_gallery"),
    path('gallery/<slug:slug>/',views.PhotoGallery.as_view(), name="photo_gallery"),
    path('history/', views.history, name="history"),
    # path('gallery/', views.gallery, name="gallery"),
    path('gallery/', views.Gallery.as_view(), name="gallery"),
    path('churches/<slug:slug>/', views.churches, name="churches"),
    # path('', views.Index.as_view(), name="index"),
    path('typography/', views.typography, name="typography"),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_us, name="contact"),
    # path('<int:year>/<int:month>/<int:date>/<slug:slug>', views.post_detail, name="post_detail"),
    # path('<int:id>/', views.post_detail, name="post_detail"),
    path('news/<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
]
