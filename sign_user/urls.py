from django.conf.urls import url
from django.urls import path
from sign_user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout_user/', views.logout_user, name="logout"),
    path('login_user/', views.login_user, name="login"),
    path('register_user/', views.register, name="register"),
    path('num1/', views.num1),
    path('num2/', views.num2),
    path('num4/', views.num4),
    path('num5/', views.num5),

    # path('login_user/', views.login_user, name="login"),
    # path('register_user/', views.register, name="register"),
    # path('sign_up/', views.sign_up, name="sign_up"),
    # path('register_user/check_username/', views.check_username, name="check_username"),
    # path('sign_in/', views.sign_in, name="sign_in"),





    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="sign_user/email_input.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="sign_user/email_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="sign_user/reset_password.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="sign_user/reset_password_success.html"),
         name="password_reset_complete"),


]
