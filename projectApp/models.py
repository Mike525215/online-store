from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='category_images/')


    def get_absolute_url(self):
        return reverse('category_items', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Items(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images/')
    price = models.IntegerField()
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

class Favourites(models.Model):
    item = models.ForeignKey(Items, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Cart(models.Model):
    item = models.ForeignKey(Items, on_delete=models.PROTECT, null=True)
    count_item = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.item.title