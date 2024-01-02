from rest_framework import serializers
from .models import CommentCourse, CommentDocument

class CommentCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentCourse
        fields = ['id', 'user', 'post', 'body', 'created_at']


class CommentDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentDocument
        fields = ['id', 'user', 'post', 'body', 'created_at']