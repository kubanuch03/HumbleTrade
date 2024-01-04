from django.urls import path
from .views import *
urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),

    path('post_lists/', PostListListView.as_view(), name='post-list-list-create'),
    path('post_lists/<int:pk>/', PostListRetrieveUpdateDestroyView.as_view(),
         name='post-list-retrieve-update-destroy'),

    path('modules/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDestroyView.as_view(), name='module-retrieve-update-destroy'),

    
]