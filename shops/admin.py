from django.contrib import admin
from .models import Image, Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
