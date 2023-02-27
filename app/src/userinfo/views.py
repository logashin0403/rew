from django.shortcuts import render, redirect
from src.users.models import CustomUser


def get_user_info(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = CustomUser.objects.get(username=username).email

        return render(request, "profile.html", context={"name": username, "email": email})
    else:
        redirect("/accounts/login/")


def update_user_info(request):
    user = CustomUser.objects.get(username=request.user.username)
    new_username = request.POST.get("username")
    new_email = request.POST.get("email")

    if request.POST.get("password1") == request.POST.get("password2") and user.check_password(request.POST.get("password1")):
        if user.username != new_username and len(new_username) != 0:
            if len(CustomUser.objects.filter(username=new_username)) == 0:
                user.username = new_username
            else:
                return render(request, "profile.html", context={'error': "Пользователь с таким именени уже существует"})
        elif user.username == new_username:
            pass
        else:
            return render(request, "profile.html", context={'error': "Поле с именем не должно быть пустым"})

        if user.email != new_email and len(new_email) != 0:
            if len(CustomUser.objects.filter(email=new_email)) == 0:
                user.email = new_email
            else:
                return render(request, "profile.html", context={'error': "Пользователь с такой почтой уже существует"})
        elif user.email == new_email:
            pass
        else:
            return render(request, "profile.html", context={'error': "Поле с почтой не должно быть пустым"})

        user.save()
        return render(request, "profile.html")
    else:
        return render(request, "profile.html", context={'error': "Пароли не совпадают или неверные"})
