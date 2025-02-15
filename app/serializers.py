from rest_framework import serializers
from .import models
from django.contrib.auth.models import User
from django.db.models import Sum


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
