# Generated by Django 4.1 on 2023-01-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ballmungApp", "0002_rename_emp_rankinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rankinfo",
            name="nickname",
            field=models.CharField(default="", max_length=100),
        ),
    ]
