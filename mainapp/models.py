from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя категории')
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract=True

    category=models.ForeignKey(Category,on_delete=models.CASCADE,
                               verbose_name='КАтегория')
    title=models.CharField(max_length=255,verbose_name='Имя продукта')
    slug=models.SlugField(unique=True)
    image=models.ImageField(verbose_name='Изображение')
    price=models.PositiveIntegerField(null=True,blank=True)


    def __str__(self):
        return self.title


class Notebook(Product):
    diagonal=models.CharField(max_length=100,verbose_name='Диагональ')
    display=models.CharField(max_length=100, verbose_name='ТИп дисплея')
    processor_freq=models.CharField(max_length=100, verbose_name='Частота процессора')
    rpm=models.CharField(max_length=100, verbose_name='Оперативная память')
    video=models.CharField(max_length=100, verbose_name='ВИдеокарта')
    time_without_charge=models.CharField(max_length=100, verbose_name='Время работы от аккамулятора')

    def __str__(self):
        return " {} : {}".format(self.category.name,self.title)

class Smartphone(Product):
    diagonal = models.CharField(max_length=100, verbose_name='Диагональ')
    display = models.CharField(max_length=100, verbose_name='ТИп дисплея')
    resolution=models.CharField(max_length=100, verbose_name='Разрешение экрана')
    accum_volume=models.CharField(max_length=100,verbose_name='Объем аккамулятора')
    rpm=models.CharField(max_length=100, verbose_name='Оперативная память')
    sd=models.BooleanField(default=True)
    sd_volume_max=models.CharField(max_length=100,verbose_name='Макс.объем встраиваемой памяти')
    frontal_camera=models.CharField(max_length=100,verbose_name='ФРонтальная камера')
    main_camera=models.CharField(max_length=100,verbose_name='Основная камера')

    def __str__(self):
        return "{} {}".format(self.category.name, self.title)






class CartProduct(models.Model):
    user=models.ForeignKey('Customer',verbose_name='Покупатель',
                           on_delete=models.CASCADE)

    cart=models.ForeignKey('Cart',on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField(null=True,blank=True)
    content_object=GenericForeignKey('content_type','object_id')
    qty=models.PositiveIntegerField(default=1)
    final_price=models.PositiveIntegerField(null=True,blank=True)


    def __str__(self):
        return 'Продукт: {}'.format(self.product.title)


class Cart(models.Model):
    owner=models.ForeignKey('Customer',on_delete=models.CASCADE)
    products=models.ManyToManyField(CartProduct,blank=True,related_name='related_cart')
    total_product=models.PositiveIntegerField(default=0)
    final_price=models.PositiveIntegerField(null=True,blank=True)




class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


    def __str__(self):
        return "Покупатель {} {}".format(self.user.first_name,
                                         self.user.last_name)

class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page( *args, **kwargs):
        with_respect_to=kwargs.get('with_respect_to')
        products=[]
        ct_models=ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products=ct_model.model_class()._base_manager.all().order_by('id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model=ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),reverse=True)
        return products




class LatestProducts:
    objects=LatestProductsManager()






