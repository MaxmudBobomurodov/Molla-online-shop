from django.core.validators import MaxValueValidator, MinValueValidator

from pages.models import BaseModel
from django.db import models


class ProductCategory(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'


class ProductSize(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product size'
        verbose_name_plural = 'product sizes'


class ProductColor(BaseModel):
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product color'
        verbose_name_plural = 'product colors'


class ProductBrand(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product brand'
        verbose_name_plural = 'product brands'


class ProductModel(BaseModel):
    title = models.CharField(max_length=128)
    short_description = models.TextField()
    long_description = models.TextField()

    image = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(ProductCategory, related_name='products')

    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=10)

    discount = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[
            MaxValueValidator(100), MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductQuantityModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='products_quantity')
    quantity = models.PositiveSmallIntegerField()

    sizes = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='products_quantity')
    colors = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='products_quantity')


class ProductImageModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
