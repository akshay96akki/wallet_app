from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_and_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()



