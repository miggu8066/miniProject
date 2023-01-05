from django.db import models

from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=255, unique=True)
    score = models.IntegerField()
    date = models.CharField(max_length=255)

    class Meta:
        db_table = 'Puzzle'
        # managed = False