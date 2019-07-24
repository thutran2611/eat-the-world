from django.db import models

#from django.contrib.auth.models import User
from apps.accounts.models import User


# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=160)
    
    def __str__(self):
        return self.name

class SavedRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    recipe_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = [['user','recipe_id']]
