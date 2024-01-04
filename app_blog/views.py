from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from .models import Post, Post_list, Module, Hashtag
from .serializers import (
    PostSerializer,
    PostListSerializer,
    ModuleSerializer,
    HashtagSerializer,
)
from .paginations import CustomPostPagination
from .permissions import IsModeratorOrReadOnly


from django_filters.rest_framework import DjangoFilterBackend


class PostListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    def get(self, request):
        return Response("Success")


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get(self, request):
        return Response("Success")


class PostListListCreateView(generics.ListCreateAPIView):
    filter_backends = [SearchFilter]
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    pagination_class = CustomPostPagination
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query = self.request.query_params.get("search", None)
        if query:
            queryset = queryset.filter(hashtags__name__icontains=query)
        return queryset


class PostListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def post(self, request):
        return Response("Success")


class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    def get(self, request):
        return Response("Success")


class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def post(self, request):
        return Response("Success")


class HashtagListCreateView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class HashtagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
