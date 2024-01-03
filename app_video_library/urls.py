from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'course', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
]
