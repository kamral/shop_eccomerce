from django.contrib import admin
from .models import *
# Register your models here.
from django import forms
from django.forms import ModelChoiceField



class NoteBookAdmin(admin.ModelAdmin):

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