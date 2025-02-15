from django.shortcuts import render

from rest_framework.views import APIView
from . import models
from rest_framework import generics
from rest_framework.views import Response
from . import serializers
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SellerListCreateAPIView(generics.ListCreateAPIView):
       serializer_class = serializers.SellerSerializer