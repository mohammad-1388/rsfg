from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    store_name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    image = serializers.ImageField(default='', use_url=True)
    fav = serializers.BooleanField(default=False)


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = '__all__' => همه را بده
        # fields = ['name', 'store_name', 'description', 'image', 'fav'] => سفارشی
        fields = '__all__'
