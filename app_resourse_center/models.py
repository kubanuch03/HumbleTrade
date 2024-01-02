from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)
    title = models.CharField(max_length=250)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title


class Document(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    post = models.FileField()
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.id}'


