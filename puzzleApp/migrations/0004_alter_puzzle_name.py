# Generated by Django 4.1 on 2023-01-09 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("puzzleApp", "0003_fileupload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puzzle",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
