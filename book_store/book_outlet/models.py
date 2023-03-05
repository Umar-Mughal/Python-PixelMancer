from django.db import models


# Create your models here.
class Book(models.Model):
    # id = models.AutoField() # it sets automatically by django
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
