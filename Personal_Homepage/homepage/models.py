from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True, default='')
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=False)


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField()


class Claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_claimed = models.DateTimeField(null= True)
    status = models.CharField(max_length=255)
