from django.shortcuts import render, redirect
from .models import Ground, Message


def grounds_list(request, sport_type):
    ground_list = Ground.objects.filter(sport_type=sport_type)
    message_list = Message.objects.all()

    areas = [
        "Приволжский", "Советский", "Ново-Савиносвкий",
        "Московский", "Вахитовский", "Кировский", "Авиастроительный"
    ]

    return render(request, "home.html", context={
        "ground_list": ground_list,
        "message_list": message_list,
        "areas": areas,
        "sport_type": sport_type
    })


def add_message(request, sport_type, ground_id):
    message = request.POST.get("message-body")

    new_message = Message()
    new_message.body = message

    if request.user.is_authenticated:
        new_message.author_name = request.user.username
    else:
        new_message.author_name = "Аноним"

    new_message.ground = Ground.objects.get(ground_id=ground_id)

    new_message.save()

    return redirect("/maps/{}".format(sport_type))
