from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import CommentCourse, CommentDocument
from .serializer import CommentCourseSerializer, CommentDocumentSerializer


class CommentsCourseViewSet(ModelViewSet):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsDocumentViewSet(ModelViewSet):
    queryset = CommentDocument.objects.all()
    serializer_class = CommentDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
