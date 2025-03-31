from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=30)   # Removed the comma
    email = models.EmailField(max_length=50)  # Increased max_length
    comments = models.CharField(max_length=255)  # Fixed missing max_length
