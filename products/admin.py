from django.contrib import admin

from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_model', 'price', 'quantity', 'category')
    fields = (
        'name', 'product_model', 'description',
        ('price', 'quantity'), 'stripe_product_price_id',
        'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
