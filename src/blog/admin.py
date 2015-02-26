from django.contrib import admin

from .models import Post


@admin.register(Post)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title", ),
    }
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'is_published')
        }),
        (None, {
            'fields': ('image', )
        }),
        ("Content", {
            'fields': ('content', )
        }),
        ("Meta", {
            'classes': ('collapse',),
            'fields': ('slug', 'meta_title', 'meta_description')
        }),
    )
    list_filter = ["is_published", ]
    list_display = ["title", "is_published"]
