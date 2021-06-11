from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name="index"),
    path('typography', views.typography, name="typography"),
    path('about', views.about_us, name="about"),
    path('contact', views.contact_us, name="contact"),
]
