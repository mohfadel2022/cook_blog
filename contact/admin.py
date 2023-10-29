from django.contrib import admin
from .models import Contact, ContactLink, About, Social, ImageAbout

class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    list_display_links = ('name',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(Social)