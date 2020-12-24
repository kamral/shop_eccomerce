from django.contrib import admin
from .models import *
# Register your models here.
from django import forms
from django.forms import ModelChoiceField,ModelForm,ValidationError
from PIL import Image

# ограничения загрузки по размеру
class NotebookAdminForm(ModelForm):

    min_resolution = (400, 400)
    max_resolution = (1000, 800)


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].help_text='Загружайте изображение с мин разрешением {} x {}'.format(
            *Product.min_resolution)

    def clean_image(self):
        image=self.cleaned_data['image']
        img=Image.open(image)
        # print(img.heigt,img.width)
        min_height, min_width=Product.min_resolution
        max_height, max_width = Product.max_resolution
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер загружаемого файла больше 3мб')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение меньше положенного')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Загруженное изображение выше положенного')
        return image

class NoteBookAdmin(admin.ModelAdmin):
    form=NotebookAdminForm

    def formfield_for_foreignkey(self, db_field,request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return  super().formfield_for_foreignkey(db_field, request, **kwargs)



class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field,request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return  super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Notebook,NoteBookAdmin)
admin.site.register(Smartphone,SmartphoneAdmin)