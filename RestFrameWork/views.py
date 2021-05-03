from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestFrameWork.models import Book
from RestFrameWork.serializers import BookModelSerializers, BookSerializers
from rest_framework import permissions
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all().order_by('-create_at')
        serializers = BookModelSerializers(query, many=True, context={'request': request})

        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_data(request):
    if request.method == "GET":
        query = Book.objects.all().order_by('-create_at')
        serializer = BookModelSerializers(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = Book.objects.filter(fav=True)
        serializers = BookModelSerializers(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class EditFavData(APIView):
    pass


class PostModelData(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializers = BookModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializers = BookSerializers(data=request.data)
        if serializers.is_valid():
            name = serializers.data.get("name")
            store_name = serializers.data.get("store_name")
            description = serializers.data.get("description")
            image = request.FILES['image']
            fav = serializers.data.get("fav")

            # Create
            book = Book()
            book.name = name
            book.store_name = store_name
            book.description = description
            book.image = image
            book.fav = fav
            book.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def set_data(request):
    if request.method == 'POST':
        serializer = BookModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['search']
        query = Book.objects.filter(store_name__contains=search)
        serializer = BookModelSerializers(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializers(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializers(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        query = Book.objects.filter(pk=pk)
        query.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)
