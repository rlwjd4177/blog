from django.db import models
from account.models import *

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank = True, null = True)

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    user = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    pup_date = models.DateTimeField()

    