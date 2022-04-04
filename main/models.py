from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.name} / {self.description} / {self.price}"

    def get_absolute_url(self):
        return reverse('post', args=[self.pk])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-time_create', 'description']


class Category(models.Model):
    name_cat = models.CharField(max_length=100, db_index=True, verbose_name="Категория")


    def __str__(self):
        return self.name_cat

    def get_absolute_url(self):
        return reverse('category', args=[self.pk])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']




