from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from marketplace.products import serializers

from marketplace.products.models import Product
from marketplace.products.serializers import CreateProductSerializer, ListProductSerializer, ModelProductSerializer
from marketplace.products.permissions import IsProductOwner
from marketplace.users.permissions import IsAdminUser, IsSellerUser

class ProductViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    List all the available products
    """

    queryset = Product.objects.filter(is_active=True)
    serializer_class = ListProductSerializer
    permission_classes = (AllowAny, )


class ProductCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """Product Create set"""

    serializer_class = CreateProductSerializer
    permission_classes = [IsProductOwner|IsAdminUser|IsSellerUser]
    queryset = Product.objects.all()



class ProductUpdateViewSet(mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """Product Update set"""
    serializer_class = ModelProductSerializer
    permission_classes = [IsProductOwner|IsAdminUser|IsSellerUser]
    queryset = Product.objects.all()
