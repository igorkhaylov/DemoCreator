from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def logout_user(request):
    logout(request)
    return render(request, "sign_user/login.html")


def login_user(request):
    return render(request, "sign_user/login.html")


def register(request):
    return render(request, "sign_user/register.html")


    # return HttpResponseRedirect("/login")


def sign_in(request):
    if request.method == "POST":
        user_name = request.POST["user"]
        user_password = request.POST["password"]
        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponse("user is active and you are logged in as a user", content_type='text/html')
                return HttpResponseRedirect("/")
            # else:
            #     print(">>>>>>>>>>>>>>>>>>>>>>>>> user is disabled")
            #     return HttpResponse("the user is disabled, please, contact to administrator", content_type='text/html')
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>> invalid login")
            # return HttpResponse("the user doesn't exist, please register again")
            return render(request, "sign_user/logout.html")
        # return HttpResponse("user successfully logged id")


def sign_up(request):
    if request.POST:
        first_nam = request.POST["first_name"]
        last_nam = request.POST["last_name"]
        user_nam = request.POST["username"]
        emai = request.POST["email_user"]
        passwor = request.POST["password"]
        User.objects.create_user(username=user_nam,
                                 first_name=first_nam,
                                 last_name=last_nam,
                                 email=emai,
                                 password=passwor,
                                 )
        user = authenticate(username=user_nam, password=passwor)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect("/")
        # print(user_nam)
        # print(first_nam)
        # print(last_nam)
        # print(emai)
        # print(passwor)
        return HttpResponseRedirect("/")


def check_username(request):
    if request.method == "GET":
        print("checkname"*10)
        username_data = request.GET["username"]
        email_data = request.GET["email_user"]
        print(username_data, email_data)
        if User.objects.filter(email=email_data):
            return HttpResponse("email exist")
        else:
            if User.objects.filter(username=username_data):
                return HttpResponse("ok", content_type='text/html')
            else:
                return HttpResponse("no", content_type='text/html')
            # return HttpResponse("email is doesn't exist")


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