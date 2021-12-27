from django.db import models
from django.contrib.auth.models import User
class Thread(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateField(auto_now_add=True)