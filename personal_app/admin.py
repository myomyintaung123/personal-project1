from django.contrib import admin
from .models import Photo, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)

