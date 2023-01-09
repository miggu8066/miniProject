from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    date = models.CharField(max_length=255)

    class Meta:
        db_table = 'Puzzle'
        # managed = False

class FileUpload(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.imgfile