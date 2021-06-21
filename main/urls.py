from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name="index"),
    path('typography', views.typography, name="typography"),
    path('about', views.about_us, name="about"),
    path('contact', views.contact_us, name="contact"),
    # path('<int:year>/<int:month>/<int:date>/<slug:slug>', views.post_detail, name="post_detail"),
    path('<int:id>/', views.post_detail, name="post_detail"),
]
