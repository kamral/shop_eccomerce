from django.db import models

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
