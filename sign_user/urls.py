from django.urls import path
from sign_user import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register/check_username/', views.check_username, name="check_username"),
    path('logout_user/', views.logout_user, name="logout"),
    path('sign_in/', views.sign_up, name="sign_in"),

]
