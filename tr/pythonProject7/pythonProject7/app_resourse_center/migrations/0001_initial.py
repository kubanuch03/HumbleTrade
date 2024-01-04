# Generated by Django 4.2.7 on 2024-01-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "slug",
                    models.SlugField(blank=True, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Document",
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
                ("image", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=250)),
                ("post", models.FileField(upload_to="")),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]
