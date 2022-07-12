from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tinymce_models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description_title = models.TextField(null=True)
    description = tinymce_models.HTMLField()
    video = models.URLField(max_length=300, default='https://www.youtube.com/embed/')
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

class FerWidget(models.Model):
    titleFer = models.CharField(max_length=255)
    descriptionFer = tinymce_models.HTMLField()
    img = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.titleFer

class ComunicationsLinks(models.Model):
    facebook = models.URLField(max_length=255, null=True)
    instagram = models.URLField(max_length=255, null=True)
    whatsapp = models.URLField(max_length=255, null=True)
    blog = models.URLField(max_length=255, null=True)
