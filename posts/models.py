from django.db import models
from datetime import datetime 
from author.models import Author

class Post(models.Model):
  author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=80)
  intro = models.CharField(max_length=80)
  body = models.TextField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  is_published = models.BooleanField(default=True)
  publish_date = models.DateTimeField(default=datetime.now, blank=True)
