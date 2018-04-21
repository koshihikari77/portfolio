from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    put_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
