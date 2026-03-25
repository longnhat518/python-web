from django.contrib import admin

# Register your models here.
from .models import Category, Artical


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "is_homepage", "layout", "ordering")
    # prepopulated_fields = {"slug": ("name",)} # Disabled to use custom JS for Vietnamese characters
    list_filter = ("is_homepage", "status", "layout")
    search_fields = ("name",)

    class Media:
        js = ("slugify.js",)


class ArticalAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "publish_date", "category")
    list_filter = ("status", "category")
    search_fields = ["name"]

    class Media:
        js = ("slugify.js",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Artical, ArticalAdmin)
