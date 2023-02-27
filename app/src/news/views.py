import datetime

from django.shortcuts import render
from .models import News, Comment
import uuid
from django.shortcuts import redirect


def news_list(request):
    new_list = News.objects.all()
    return render(request, "news.html", context={"new_list": new_list})


def add_news(request):
    title = request.POST.get("title")
    body = request.POST.get("body")

    image_from_form = request.FILES["photo"]
    image_format = image_from_form.name.split(".")[-1].lower()
    correct_image_format = ["jpg", "png", "jpeg"]

    if image_from_form is not None and image_format in correct_image_format and len(title) != 0 and len(body) != 0:
        new_post = News()

        if request.user.is_authenticated:
            new_post.author_name = request.user.username
        else:
            new_post.author_name = "Аноним"

        new_post.title = title
        new_post.body = body
        new_post.photo_url.save(f"{str(uuid.uuid4())}.{image_format}", image_from_form)

        new_post.photo_url = str(new_post.photo_url).replace("static/", "")

        new_post.save()
        return render(request, "news.html")
    else:
        return render(request, "news.html", context={"error": "Ошибка в заполнении формы"})


def read_news(request, news_id):
    obj = News.objects.get(news_id=news_id)
    comments = Comment.objects.filter(post_id=news_id)
    return render(request, "personal_news.html", context={"obj": obj, "comments": comments})


def add_comment(request, news_id):
    comment = Comment()
    comment.body = request.POST.get("body")
    comment.created = datetime.datetime.now()

    if request.user.is_authenticated:
        comment.author_name = request.user.username
    else:
        comment.author_name = "Аноним"

    comment.post = News.objects.get(news_id=news_id)

    comment.save()
    return redirect("/news/" + str(news_id) + "/")
