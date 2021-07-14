from django.urls import path
from sign_user import views


urlpatterns = [
    path('login_user/', views.logout_user, name="logout"),
    path('login_user/', views.login_user, name="login"),
    path('register_user/', views.register, name="register"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register_user/check_username/', views.check_username, name="check_username"),
    path('sign_in/', views.sign_in, name="sign_in"),
    # path('login_user/check_login/', views.check_login, name="check_login")
]
