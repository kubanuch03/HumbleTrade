from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import *
from .pagination import CustomPageNumberPagination
from .serializers import (
    CategorySerializer,
    CourseSerializers,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"


class CourseViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializers
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"
