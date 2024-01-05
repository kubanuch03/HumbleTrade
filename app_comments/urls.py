from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentsCourseViewSet, CommentsDocumentViewSet

router = DefaultRouter()
router.register(
    r"video/library/course",
    CommentsCourseViewSet,
    basename="comments-video-library-course",
)
router.register(
    r"resourse/center/document",
    CommentsDocumentViewSet,
    basename="comments-resourse-center-documents",
)

urlpatterns = [
    path("", include(router.urls)),
]
