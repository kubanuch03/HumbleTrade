from rest_framework import generics
from rest_framework import permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        post_list_id = self.kwargs['post_list_id']
        return Comment.objects.filter(post__id=post_list_id)

    def perform_create(self, serializer):
        post_list_id = self.kwargs['post_list_id']
        serializer.save(post_id=post_list_id, author=self.request.user)
