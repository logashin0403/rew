from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    news_id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    photo_url = models.ImageField(upload_to='static/media/news-images/')

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("read_news", kwargs={"news_id": self.news_id})


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    body = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
