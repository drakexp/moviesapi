from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
   title = models.CharField(max_length=100)
   rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
      ) 

   def __str__(self):
        return self.title