from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Unit, Lesson, StrategyCourse, StrategyLesson
from .seriallizer import (CourseSerializer,
    LessonSerializer,
    StrategyCourseSerializer,
    StrategyLessonSerializer
 )
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser]



class StrategyLessonViewSet(ModelViewSet):
    queryset = StrategyLesson.objects.all()
    serializer_class = StrategyLessonSerializer
    permission_classes = [permissions.IsAdminUser]



class StrategyCourseViewSet(ModelViewSet):
    queryset = StrategyCourse.objects.all()
    serializer_class = StrategyCourseSerializer
    permission_classes = [permissions.IsAdminUser]



class DownloadDocumentView(View):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        document = get_object_or_404(StrategyLesson, pk=pk)
        if not document.lesson:
            raise Http404("Файл не найден")
        response = FileResponse(document.lesson, as_attachment=True)
        response["Content-Disposition"] = f"attachment; filename={document.lesson.name}"
        return response