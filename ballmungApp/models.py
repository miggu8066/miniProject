from django.db import models

class rankInfo(models.Model):
    nickname = models.CharField(max_length=100, default="")
    score = models.IntegerField()
    clearTime = models.IntegerField()
    regiDate = models.CharField(max_length=100)

# Create your models here.
