from django.db import models


class Ground(models.Model):
    ground_id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    underground_station = models.CharField(max_length=100)
    photo_url = models.ImageField(upload_to='static/media/grounds-images/')
    sport_type = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    free_area = models.BooleanField(default=True)


class Message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    body = models.CharField(max_length=200)
    created = models.TimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
