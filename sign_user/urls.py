from django.conf.urls import url
from django.urls import path
from sign_user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user/', views.logout_user, name="logout"),
    path('login_user/', views.login_user, name="login"),
    path('register_user/', views.register, name="register"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register_user/check_username/', views.check_username, name="check_username"),
    path('sign_in/', views.sign_in, name="sign_in"),


    # path('password_reset_form/', views.passwor_reset_form, name='password_reset_form'),

    # path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset', ),
    # path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done', ),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm', ),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete', ),

    # url(r'^passreset/$', auth_views.password_reset, name='forgot_password1'),
    # url(r'^passresetdone/$', auth_views.password_reset_done, name='forgot_password2'),
    # url(r'^passresetconfirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
    #     name='forgot_password3'),
    # url(r'^passresetcomplete/$', auth_views.password_reset_complete, name='forgot_password4'),
    # url(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    # url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),

    # path('login_user/check_login/', views.check_login, name="check_login")
]
