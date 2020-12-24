from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
from django.urls import reverse


class Category(models.Model):

    name=models.CharField(max_length=100,verbose_name='Категории')
    slug=models.SlugField(unique=True)
    # objects=CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})

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


class Customers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


    def __str__(self):
        return "Покупатель {} {}".format(self.user.first_name,
                                         self.user.last_name)

