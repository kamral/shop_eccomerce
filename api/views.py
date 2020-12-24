from django.shortcuts import render
from .serializers import CategorySerializers,SmartphoneSerializer,CustomersSerializers
# Create your views here.
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Category,Smartphone,Customers

from rest_framework.filters import SearchFilter

class CategoryListAPiView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()



class SmartphoneListAPiVIew(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()

    # переопраделеяем queryset
    #
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     price,title=self.request.query_params.get('price'),self.request.query_params.get('title')
    #     search_params={'price__iexact':price,'title__iexact':title}
    #     return qs.filter(**search_params)
    # ?search=65000
    # ?search=iphone1
    filter_backends = [SearchFilter]
    search_fields=['price','title']

class SmartDetailApiView(RetrieveAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()


class CustomerListApiView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Customers.objects.all()