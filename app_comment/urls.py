from django.urls import path
from .views import *

urlpatterns = [
    # Добавляем маршрут для списка и создания комментариев к постлисту
    path('post_lists/<int:post_list_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    # Добавьте другие маршруты для обновления, удаления, получения комментариев по их id, если необходимо
]
