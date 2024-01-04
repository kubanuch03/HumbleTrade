from django.urls import path, include
from .views import (
    UnitViewSet,
    LessonViewSet,
    StrategyCourseViewSet,
    StrategyLessonViewSet,
    DownloadDocumentView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"unit", UnitViewSet, basename="course_crud")
router.register(r"lesson", LessonViewSet, basename="lesson_crud")
router.register(
    r"strategy/course", StrategyCourseViewSet, basename="6 sessistrategy crush course"
)
router.register(
    r"strategy/lesson",
    StrategyLessonViewSet,
    basename="6 sessistrategy crush course lesson",
)
# router.register(r'download/document/<int:pk>/', DownloadDocumentView, basename='downloads-documents')


urlpatterns = [
    path("", include(router.urls)),
    path("download/<int:pk>/", DownloadDocumentView.as_view(), name="download-file"),
]
