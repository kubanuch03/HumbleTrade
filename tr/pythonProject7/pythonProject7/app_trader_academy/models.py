from django.db import models
from app_clients.models import Client


class Unit(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField()
    instructor = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.id}"


class StrategyCourse(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.id}"


class StrategyLesson(models.Model):
    course = models.ForeignKey(StrategyCourse, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField()
    instructor = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.title}"
