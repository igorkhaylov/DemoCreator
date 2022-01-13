from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from .decorators import unauthenticated_user
from django.http import HttpResponse, HttpResponseRedirect, BadHeaderError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import PasswordResetForm
# Create your views here.
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import send_mail


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            # passwordmy = form.cleaned_data.get("password1")

            messages.success(request, f"Аккаунт {username} был успешно создан")
            # f"{passwordmy} это будет пароль его")
            return redirect("login")
        else:
            # messages.info(request, "Логин должен содержать только буквы, цифры и символы"
            #                        "Пароль должен содержать минимум 8 символов"
            #                        "Пароль не должен быть слишком простым"
            #                        "Пароль не может состоять только из цифр")
            messages.error(request,
                           "Ошибка регистрации, проверьте правильность введенной информации или поменяйте логин")
            # messages.success(request, "Удачно")
    return render(request, "sign_user/registration_form.html", {"form": form})


@unauthenticated_user
def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # print(f"{username} это у нас будет имя и пароль вот такой")
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Логин или Пароль не верны")
    return render(request, "sign_user/sign_in_form.html", {"form": form})


def logout_user(request):
    logout(request)
    return render(request, "sign_user/sign_in_form.html")

# return HttpResponseRedirect("/login")

# def sign_in(request):
#     if request.method == "POST":
#         user_name = request.POST["user"]
#         user_password = request.POST["password"]
#         user = authenticate(username=user_name, password=user_password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # return HttpResponse("user is active and you are logged in as a user", content_type='text/html')
#                 return HttpResponseRedirect("/")
#             # else:
#             #     print(">>>>>>>>>>>>>>>>>>>>>>>>> user is disabled")
#             #     return HttpResponse("the user is disabled, please, contact to administrator", content_type='text/html')
#         else:
#             print(">>>>>>>>>>>>>>>>>>>>>>> invalid login")
#             # return HttpResponse("the user doesn't exist, please register again")
#             return render(request, "sign_user/logout.html")
#         # return HttpResponse("user successfully logged id")


# def sign_up(request):
#     if request.POST:
#         first_nam = request.POST["first_name"]
#         last_nam = request.POST["last_name"]
#         user_nam = request.POST["username"]
#         emai = request.POST["email_user"]
#         passwor = request.POST["password"]
#         User.objects.create_user(username=user_nam,
#                                  first_name=first_nam,
#                                  last_name=last_nam,
#                                  email=emai,
#                                  password=passwor,
#                                  )
#         user = authenticate(username=user_nam, password=passwor)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # return HttpResponseRedirect("/")
#         # print(user_nam)
#         # print(first_nam)
#         # print(last_nam)
#         # print(emai)
#         # print(passwor)
#         return HttpResponseRedirect("/")


# def check_username(request):
#     if request.method == "GET":
#         print("checkname"*10)
#         username_data = request.GET["username"]
#         email_data = request.GET["email_user"]
#         print(username_data, email_data)
#         if User.objects.filter(email=email_data):
#             return HttpResponse("email exist")
#         else:
#             if User.objects.filter(username=username_data):
#                 return HttpResponse("ok", content_type='text/html')
#             else:
#                 return HttpResponse("no", content_type='text/html')
#             # return HttpResponse("email is doesn't exist")


# def check_login(request):
#     if request.method == "GET":
#         username = request.GET["username"]
#         password = request.GET["password"]
#         user = authenticate(username=username, password=password)
#         print("check login user")
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse("yes", content_type='text/html')
#             # else:
#             #     print(">>>>>>>>>>>>>>>>>>>>>>>>> user is disabled")
#             #     return HttpResponse("the user is disabled, please, contact to administrator", content_type='text/html')
#         else:
#             # print(">>>>>>>>>>>>>>>>>>>>>>> invalid login")
#             return HttpResponse("no", content_type='text/html')
#
# pass

# def passwor_reset_form(request):
#     return render(request, "sign_user/password_reset.html")


# import requests
# BOT_TOKEN = '1873821132:AAEPwFu0ESTuEhLNDF5di1nxukhxDXzmUh4'
# admin_id = '432499122'
#
# def password_reset_request(request):
#     if request.method == "POST":
#         print('post'*100)
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             mail = password_reset_form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=mail)
#             except Exception:
#                 user = False
#             if user:
#                 subject = "Запрошен сброс пароля"
#                 email_template_name = "sign_user/password_reset_msg.html"
#                 cont = {
#                     "email": user.email,
#                     "domain": '192.168.0.105:80',
#                     "site_name": "igorkhaylov",
#                     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                     "user": user,
#                     "token": default_token_generator.make_token(user),
#                     "protocol": "http",
#                 }
#                 msg_html = render_to_string(email_template_name, cont)
#                 try:
#                     def teleg(BOT_TOKEN, admin_id, message):
#                         url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={admin_id}&parse_mode=HTML&text={message}'
#                         response = requests.get(url)
#                         return response.json()
#                     response = teleg(BOT_TOKEN, admin_id, msg_html)
#                     # send_mail(subject, 'ссылка', 'igorkhaylov@yandex.com', [user.email], fail_silently=True, html_message=msg_html)
#                 except BadHeaderError:
#                     return HttpResponse("Обнаружен недопустимый заголовок")
#                 return redirect("password_reset_done")
#             else:
#                 messages.error(request, 'Пользователь не найден, напишите проблему администратору')
#                 return HttpResponseRedirect("/")
#         return render(request, "sign_user/login.html")
