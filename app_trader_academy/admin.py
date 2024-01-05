from django.contrib import admin
from .models import Unit, Lesson, StrategyCourse, StrategyLesson

admin.site.register(Lesson)
admin.site.register(Unit)
admin.site.register(StrategyCourse)
admin.site.register(StrategyLesson)
