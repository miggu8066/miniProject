# Generated by Django 4.1 on 2023-01-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Space_shooting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, null=True)),
                ("score", models.IntegerField()),
                ("time_info", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]