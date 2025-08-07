# admin.py
from django.contrib import admin
from .models import (
    ProductCategory, ProductSize, ProductColor, ProductBrand,
    ProductModel, ProductQuantityModel, ProductImageModel
)


# Inline classes for ProductModel
class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1  # Number of empty forms to display
    fields = ('image',)


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantityModel
    extra = 1  # Number of empty forms to display
    fields = ('quantity', 'sizes', 'colors')


# Main admin class for ProductModel
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'discount')
    list_filter = ('brand', 'categories')
    search_fields = ('title', 'brand__name')
    filter_horizontal = ('categories',)

    inlines = [ProductImageInline, ProductQuantityInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'brand', 'categories')
        }),
        ('Description', {
            'fields': ('short_description', 'long_description')
        }),
        ('Pricing', {
            'fields': ('price', 'discount')
        }),
        ('Main Image', {
            'fields': ('image',)
        }),
    )


# Register other models
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ('title',)
    list_editable = ('code',)


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# # Optional: If you want to hide the inline models from appearing separately in admin
# # You can choose not to register them individually, or register them with limited access
# @admin.register(ProductImageModel)
# class ProductImageModelAdmin(admin.ModelAdmin):
#     list_display = ('product', 'image')
#     list_filter = ('product',)
#
#
# @admin.register(ProductQuantityModel)
# class ProductQuantityModelAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity', 'sizes', 'colors')
#     list_filter = ('product', 'sizes', 'colors')
#     search_fields = ('product__title',)