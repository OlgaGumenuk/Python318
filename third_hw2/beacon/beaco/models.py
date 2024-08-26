from django.db import models
from django.contrib.auth.models import User


class Beaco(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)  # blank=True не обязательно заполнять
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)  # будет заполнятся null этим
    important = models.BooleanField(default=False)  # default-по умолчанию если галочку то изменяется на True
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

