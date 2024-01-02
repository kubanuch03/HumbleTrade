from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class StrategyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyCourse
        fields = '__all__'


class StrategyLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyLesson
        fields = '__all__'