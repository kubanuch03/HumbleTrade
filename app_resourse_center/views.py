from .models import *
from .serializer import CategorySerializers, DocumentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.http import Http404
from app_video_library.pagination import CustomPageNumberPagination
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAdminUser]

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = CustomPageNumberPagination
    permission_classes = [AllowAny, ]


class CategoryDeleteApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        message = "успешно удалено"
        return Response(str(message), status=status.HTTP_204_NO_CONTENT)


class CategoryPutApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = CategorySerializers(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentCreateApiView(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAdminUser]


class DocumentListApiView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [AllowAny,]


class DocumentDeleteApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        message = "успешно удалено"
        return Response(str(message), status=status.HTTP_204_NO_CONTENT)


class DocumetPutApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = DocumentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadFileView(View):
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        if not document.post:
            raise Http404("Файл не найден")
        response = FileResponse(document.post, as_attachment=True)
        response["Content-Disposition"] = f"attachment; filename={document.post.name}"
        return response

    permission_classes = [permissions.AllowAny]
