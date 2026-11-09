
# Register your models here.
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'garment_type', 'color', 'available', 'created_at']
    list_filter = ['available', 'category', 'garment_type']
    list_editable = ['price', 'available']
    search_fields = ['name', 'description', 'color']
    prepopulated_fields = {'slug': ('name',)}