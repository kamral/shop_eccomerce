from django.urls import path
from .views import CategoryListAPiView,\
    SmartphoneListAPiVIew,\
    SmartDetailApiView,CustomerListApiView


urlpatterns=[
    path('categories/', CategoryListAPiView.as_view()),
    path('smartphones/', SmartphoneListAPiVIew.as_view()),
    path('smartphones/<int:pk>/', SmartDetailApiView.as_view()),
    path('customers/', CustomerListApiView.as_view())

]