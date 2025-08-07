from django.contrib import admin
from .models import BlogCategory, BlogModel


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_categories', 'created_at', 'updated_at')
    list_filter = ('author', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'long_description')
    autocomplete_fields  = ('category',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author')
        }),
        ('Content', {
            'fields': ('long_description', 'comment', 'image')
        }),
        ('Categories', {
            'fields': ('category',)
        }),
    )

    def get_categories(self, obj):
        """Display categories in list view"""
        return obj.category.title

    get_categories.short_description = 'Categories'

    # Optional: Add readonly fields if you want to display created/updated timestamps
    # readonly_fields = ('created_at', 'updated_at')

# Alternative registration method (if you prefer not using decorators):
# admin.site.register(BlogCategory, BlogCategoryAdmin)
# admin.site.register(BlogModel, BlogModelAdmin)