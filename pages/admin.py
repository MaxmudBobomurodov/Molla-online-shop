from django.contrib import admin
from pages.models import ContactModel, StoreModel
from modeltranslation.admin import TranslationAdmin


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    list_filter = ['created_at', 'is_read']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created_at']

@admin.register(StoreModel)
class StoreModelAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'address', 'created_at']
    list_filter = ['created_at', 'picked']
    search_fields = ['name', 'address']
    ordering = ['-created_at']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }