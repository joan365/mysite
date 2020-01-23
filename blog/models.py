from django.db import models
from random import randrange

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def resum(self):
        if (len(self.text) / 2) > 200:
            long = len(self.text) * 25 / 100
        elif len(self.text) > 200:
            long = randrange(90, 150)
        elif len(self.text) > 20:
            long = randrange(20, 90)
        else:
            #long = len(self.tetx) - 1
            long = 0

        if long > 0:
            return self.text[:int(long)] + "..."
        else:
            return "..."
