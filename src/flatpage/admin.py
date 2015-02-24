from django.contrib import admin

from suit.admin import SortableModelAdmin

from .forms import FlatpageForm
from .models import FlatPage


class FlatPageAdmin(SortableModelAdmin):
    form = FlatpageForm
    prepopulated_fields = {
        "meta_title": ("title",),
        "meta_description": ("description",),
    }
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'description', 'is_published')
        }),
        (None, {
            'fields': ('image', 'image_caption'),
        }),
        (None, {
            'fields': ('content',)
        }),
        (None, {
            'fields': ('sidebar',)
        }),
        ("Meta", {
            'classes': ('collapse', 'wide'),
            'fields': ('template_name', 'meta_title', 'meta_description')
        })
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title', 'subtitle')

    # Django suit
    sortable = 'ordering'


admin.site.register(FlatPage, FlatPageAdmin)