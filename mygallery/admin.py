from django.contrib import admin

from .models import CategoryModel, ImageModel, LocationModel

class ImageModelAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'category', 'location',"description", "id","file"]


class CategoryModelAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name',  "id"]

class LocationModelAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', "id"]

# Register your models here.
admin.site.register(ImageModel,ImageModelAdmin)
admin.site.register(LocationModel,LocationModelAdmin)
admin.site.register(CategoryModel,CategoryModelAdmin)