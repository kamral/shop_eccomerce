from django.urls import path
from .views import CategoryListAPiView,SmartphoneListAPiVIew


urlpatterns=[
    path('categories/', CategoryListAPiView.as_view()),
    path('smartphones/', SmartphoneListAPiVIew.as_view())

]