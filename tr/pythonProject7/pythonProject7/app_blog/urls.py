from django.urls import path
from .views import (
    PostListCreateView,
    PostListListCreateView,
    PostListRetrieveUpdateDestroyView,
    PostRetrieveUpdateDestroyView,
    ModuleListCreateView,
    ModuleRetrieveUpdateDestroyView,
    HashtagRetrieveUpdateDestroyView,
    HashtagListCreateView,
)

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path(
        "posts/<int:pk>/",
        PostRetrieveUpdateDestroyView.as_view(),
        name="post-retrieve-update-destroy",
    ),
    path("post_lists/", PostListListCreateView.as_view(), name="post-list-list-create"),
    path(
        "post_lists/<int:pk>/",
        PostListRetrieveUpdateDestroyView.as_view(),
        name="post-list-retrieve-update-destroy",
    ),
    path("modules/", ModuleListCreateView.as_view(), name="module-list-create"),
    path(
        "modules/<int:pk>/",
        ModuleRetrieveUpdateDestroyView.as_view(),
        name="module-retrieve-update-destroy",
    ),
    path("hashtags/", HashtagListCreateView.as_view(), name="hashtag-list"),
    path(
        "hashtags/<int:pk>/",
        HashtagRetrieveUpdateDestroyView.as_view(),
        name="hashtag-detail",
    )
    # Другие URL-адреса вашего приложения
]
