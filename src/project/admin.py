from django.contrib import admin

from suit.admin import SortableModelAdmin
from suit.admin import SortableStackedInline

from .models import Client, Category, Project, ProjectImage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProjectImageInline(SortableStackedInline):
    model = ProjectImage
    extra = 0
    sortable = 'ordering'


@admin.register(Project)
class ProjectAdmin(SortableModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [ProjectImageInline, ]
    filter_horizontal = ["categories", ]
    list_filter = ["client", "is_published"]
    list_display = ["name", "is_published"]
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'client', 'categories', 'is_published')
        }),
        (None, {
            'fields': ('landscape_image', 'portrait_image', )
        }),
        (None, {
            'fields': ('content', )
        }),
        ("Meta", {
            'fields': ('slug', 'meta_title', 'meta_description')
        })
    )

    # Django suit
    sortable = 'ordering'
