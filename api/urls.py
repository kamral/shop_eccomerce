from django.urls import path
from .views import CategoryListAPiView


urlpatterns=[
    path('categories/', CategoryListAPiView.as_view())
]