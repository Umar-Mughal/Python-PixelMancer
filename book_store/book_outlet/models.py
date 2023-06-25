from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    # id = models.AutoField() # it sets automatically by django
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)
