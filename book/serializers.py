from rest_framework import serializers
from rest_framework.response import Response
from .models import Book, BookOrder, BookShopItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "description", "price", "image_url")
        read_only_fields = ("id", )

class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookShopItem
        fields = ("book", "quantity")

class BookOrderSerializer(serializers.ModelSerializer):
    items = BookItemSerializer(many=True)

    class Meta:
        model = BookOrder
        fields = ("state", 'items', 'billing_address', 'billing_name', 'billing_phone')
        read_only_fields = ('state', )

    def create(self, validated_data):
        order = BookOrder.objects.create()
        items = validated_data['items']

        for item in items:
            BookShopItem.objects.create(order=order, book=item['book'], quantity=item['quantity']) 

        return order

    def validate(self, data):
        items = data['items']
        if len(items) == 0:
            raise serializers.ValidationError("Shop items could not be empty")

        return data

class BookOrderCreateSerializer(BookOrderSerializer):
    items = BookItemSerializer(many=True)

    class Meta:
        model = BookOrder
        fields = ('state', 'items', 'pay_url')
        read_only_fields = ('state', )
