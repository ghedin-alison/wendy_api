from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.Charfield(max_lenght=200)
    image = models.Charfield(max_lenght=200)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass