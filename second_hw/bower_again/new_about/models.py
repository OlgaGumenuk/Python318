from django.db import models


class New_about(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='new_about/images/')
    url = models.URLField(blank=True)