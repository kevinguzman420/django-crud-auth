from django.db import models
from django.contrib.auth.models import User


# username: kevin333
# email: kevin@gmail.com
# password: kevin333


# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.title + " - by " + self.user.username
