from rest_framework import serializers

from book_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=250, required=True)
    author = serializers.CharField(max_length=100, required=True)
    price = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = ['id','title','author','price']