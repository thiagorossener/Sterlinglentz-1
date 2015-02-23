from django.contrib import admin

from .models import Post


@admin.register(Post)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title", ),
        "meta_title": ("title", )
    }
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'image', 'is_published')
        }),
        ("Content", {
            'fields': ('content', )
        }),
        ("Advanced", {
            'fields': ('slug', )
        }),
        ("Meta", {
            'fields': ('meta_title', 'meta_description')
        }),
    )
    list_filter = ["is_published", ]
    list_display = ["title", "is_published"]
