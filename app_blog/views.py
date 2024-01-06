from rest_framework import generics
from .models import Post, Post_list, Module, Hashtag
from .serializers import (
    PostSerializer,
    PostListSerializer,
    ModuleSerializer,
    HashtagSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPostPagination
from .permissions import IsModeratorOrReadOnly

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import NotFound

from drf_spectacular.utils import extend_schema


class PostListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = self.queryset
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="List a  blog post list",
        description="List a  blog post list",
        request=PostSerializer,
        responses={200: PostSerializer},
        operation_id="blog_post_list_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new blog post list",
        description="Create a new blog post list",
        request=PostSerializer,
        responses={201: PostSerializer},
        operation_id="blog_post_create_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


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

    @extend_schema(
        summary="Post_List List  a blog post list",
        description="Post_List List a  blog post list",
        request=PostListSerializer,
        responses={200: PostListSerializer},
        operation_id="list_blog_post_lst_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=" Post_lst Create a new blog post lst",
        description="Post_lst Create a new blog post lst",
        request=PostListSerializer,
        responses={201: PostListSerializer},
        operation_id="create_blog_post_lst_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_list.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsModeratorOrReadOnly]

    @extend_schema(
        summary=" Post_lst RUD a  blog post lst",
        description="Post_lst RUD a  blog post lst",
        request=PostListSerializer,
        responses={200: PostListSerializer},
        operation_id="rud_blog_post_lst_v1",
    )
    def post(self, request):
        return Response("Success")


class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly, permissions.IsAuthenticated]

    @extend_schema(
        summary="List a  blog module",
        description="List a  blog module",
        request=ModuleSerializer,
        responses={200: ModuleSerializer},
        operation_id="blog_module_list_v1",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new blog module",
        description="Create a new blog module",
        request=ModuleSerializer,
        responses={201: ModuleSerializer},
        operation_id="blog_module_create_v1",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get(self, request):
        return Response("Success")


class ModuleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsModeratorOrReadOnly]

    @extend_schema(
        summary="RUD a new blog module",
        description="RUD a new blog module",
        request=ModuleSerializer,
        responses={201: ModuleSerializer},
        operation_id="blog_module_post_v1",
    )
    def post(self, request):
        return Response("Success")


class HashtagListCreateView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    @extend_schema(
        summary="Get a success message",
        description="Get a success message",
        responses={200: "Success"},
        operation_id="blog_hashtag_get_success_v1",
    )
    def get(self, request):
        return Response("Success")


class HashtagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
