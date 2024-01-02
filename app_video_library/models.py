from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    image = models.ImageField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title



class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField()
    video_library = models.FileField(upload_to='videos/')

    def str(self):
        return f'{self.image}, {self.title}, {self.description}'

    