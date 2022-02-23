from rest_framework import serializers
from .models import Product


class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'owner')


class ModelProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'quantity',
            'is_active',
            'owner'
        )
        read_only_fields = ('owner', )


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'quantity',
            'is_active'
        )

    def create(self, validated_data):
        print(self.context)
        product = Product.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            quantity=validated_data['quantity'],
            is_active=validated_data['is_active'],
            owner=self.context['request'].user
        )

        return product