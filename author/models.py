from django.db import models
from datetime import datetime 


class Author(models.Model):
  name = models.CharField(max_length=150)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description= models.TextField()
  email = models.CharField(max_length=50, blank=True)
  linkedin = models.CharField(max_length=100, blank=True)
  github = models.CharField(max_length=100, blank=True)
  def __str__(self):
    return self.name
