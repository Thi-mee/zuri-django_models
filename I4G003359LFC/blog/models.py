from django.db import models
from django.conf import settings

# Create your models here.
class blog(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(
      settings.AUTH_USER_MODEL,  # new
      on_delete=models.CASCADE
    )
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()