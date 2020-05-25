from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank = True, null = True)

    def summary(self):
        return self.body[:100]