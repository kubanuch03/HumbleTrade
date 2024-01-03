from .models import Post, Post_list, Module
from .serializers import PostSerializer, PostListSerializer, ModuleSerializer
from .paginations import CustomPostPagination
from .permissions import IsModeratorOrReadOnly

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

class PostListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hashtags__name']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # Your implementation here
        return Response("Success")
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get(self, request):
        # Your implementation here
        return Response("Success")
    
class PostListListCiew(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hashtags__name']
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    pagination_class = CustomPostPagination
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Your implementation here
        return Response("Success")

class PostListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAdminUser]

    def get(self, request):
        # Your implementation here
        return Response("Success")
    


class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAdminUser]

    def get(self, request):
        # Your implementation here
        return Response("Success")

class ModuleListView(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get(self, request):
        # Your implementation here
        return Response("Success")