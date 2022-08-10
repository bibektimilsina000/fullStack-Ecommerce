from rest_framework import serializers

from .models import Category, Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = (
            "id",
            "name",
            "get_absolute_url",
            "despriction",
            "price",
            "get_image",
            "get_thumbnail",
        )


class CategorySeiralizers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )
