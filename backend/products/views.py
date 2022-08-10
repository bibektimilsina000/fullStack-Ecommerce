from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializers, CategorySeiralizers


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]

        serializers = ProductSerializers(products, many=True)

        return Response(serializers.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(Category__slug=category_slug).get(
                slug=product_slug
            )
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializers(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySeiralizers(category)
        return Response(serializer.data)


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(despriction__icontains=query)
        )
        serializers = ProductSerializers(products, many=True)

        return Response(serializers.data)
    else:
        return Response({"products": []})


def cart(request):
    pass
