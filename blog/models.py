from django.db import models
from django.conf import settings


class Blogger(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
