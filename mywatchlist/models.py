from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class MyWatchList(models.Model): # model di Django kayak translator, misal dia translate ke SQL buat dapetin data yang dinginkan dari database
    watched = models.BooleanField()
    title = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    release_date = models.DateField()
    review = models.TextField()

    # blg kayak MyWatchList punya attribute watched, title, rating, dll, ini jd kayak template gt