from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'id']
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']

@admin.register(models.Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'created_at']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)