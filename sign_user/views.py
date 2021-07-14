from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login(request):
    return render(request, "sign_user/login.html")


def register(request):
    return render(request, "sign_user/register.html")


def logout_user(request):
    logout(request)
    return render(request, "sign_user/login.html")


def sign_up(request):
    if request.POST:
        first_nam = request.POST["first_name"]
        last_nam = request.POST["last_name"]
        user_nam = request.POST["username"]
        emai = request.POST["email"]
        passwor = request.POST["password"]
        User.objects.create_user(username=user_nam,
                                 first_name=first_nam,
                                 last_name=last_nam,
                                 email=emai,
                                 password=passwor,
                                 )
        # print(user_nam)
        # print(first_nam)
        # print(last_nam)
        # print(emai)
        # print(passwor)
        return HttpResponseRedirect("/login")


def check_username(request):
    if request.method == "GET":
        print("checkname"*10)
        username = request.GET["username"]
        print(username)
        if User.objects.filter(username=username):
            return HttpResponse("ok", content_type='text/html')
        else:
            return HttpResponse("no", content_type='text/html')
    # return HttpResponseRedirect("/login")



def sign_in(request):
    user_name = request.POST["user_name"]
    user_password = request.POST["password"]
    user = authenticate(username=user_name, password=user_password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>> user is disabled")
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>> invalid login")
    return HttpResponseRedirect("/")
