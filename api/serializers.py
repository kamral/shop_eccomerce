from rest_framework import serializers
from .models import Category,Smartphone


class CategorySerializers(serializers.ModelSerializer):

    name=serializers.CharField(required=True)
    slug=serializers.SlugField()

    class Meta:
        model=Category
        fields=[
           'id', 'name','slug'
        ]


# сериализатор для абстрактного класса
class BaseProductSerializer:
    # category=models.Foreignkey(Category,verbose_name='Категория')
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    # title=models.CharField(max_length=100, verbose_name='Название')
    title=serializers.CharField(required=True)
    # slug=models.SlugField(unique=True)
    slug=serializers.SlugField(required=True)
    # image=models.ImageField(verbose_name='Изображения')
    image=serializers.ImageField(required=True)
    # description=models.TimeField(verbose_name='Описание',тгдд=True)
    description=serializers.CharField(required=True)
    # price=models.PositiveIntegerField(null=True, blank=True)
    price=serializers.IntegerField(required=True)

# наследуем от верхнего класа
class SmartphoneSerializer(BaseProductSerializer,serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display = serializers.CharField(required=True)
    resolution = serializers.CharField(required=True)
    accum_volume = serializers.CharField(required=True)
    rpm = serializers.CharField(required=True)
    sd = serializers.BooleanField(default=True)
    sd_volume_max = serializers.CharField(required=True)
    frontal_camera = serializers.CharField(required=True)
    main_camera = serializers.CharField(required=True)

    class Meta:
        model=Smartphone
        fields='__all__'
