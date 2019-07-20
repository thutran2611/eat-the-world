from django.db import models

# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=160)
    
    def __str__(self):
        return self.name
