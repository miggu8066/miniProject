from django.db import models

class Space_shooting(models.Model):
    name = models.CharField(max_length=10,null=True)
    score = models.IntegerField()
    time_info = models.CharField(max_length=100,null=True)
    class Meta:
    #     db_table = 'space_shooting'
        managed = False
