from django.urls import path
from .views import *


urlpatterns = [
    
    path("category/create/list/", CategoryCreateApiView.as_view()),
    path("category/delete/<int:pk>/", CategoryDeleteApiView.as_view()),
    path("category/put/<int:pk>/", CategoryPutApiView.as_view()),

    path("document/create/list/", DocumentCreateApiView.as_view()),
    path("document/delete/<int:pk>/", DocumentDeleteApiView.as_view()),
    path("document/put/<int:pk>/", DocumetPutApiView.as_view()),

    path("download/<int:pk>/", DownloadFileView.as_view(), name="download-file"),
]
