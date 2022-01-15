from django.conf.urls import url
from django.urls import path
from sign_user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout_user/', views.logout_user, name="logout"),
    path('login_user/', views.login_user, name="login"),
    path('register_user/', views.register, name="register"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="sign_user/email_input.html", html_email_template_name="sign_user/password_reset_email.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="sign_user/email_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="sign_user/reset_password.html"),
         name="password_reset_confirm"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(email_template_name="sign_user/password_reset_email.html"),
    #      path('password_reset/', auth_views.PasswordResetView.as_view(),
    #           name="password_reset"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="sign_user/reset_password_success.html"),
         name="password_reset_complete"),

]
