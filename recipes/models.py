from django.db import models
from django.contrib.auth.models import User  

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    img = models.ImageField(upload_to='recipe_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time_of_execution = models.IntegerField(default=0)  

    def __str__(self):
        return self.title