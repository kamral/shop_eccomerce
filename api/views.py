from django.shortcuts import render
from .serializers import CategorySerializers
# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Category

class CategoryListAPiView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

