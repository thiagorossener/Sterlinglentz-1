from django.contrib import admin

from suit.admin import SortableModelAdmin

from .forms import FlatpageForm
from .models import FlatPage


class FlatPageAdmin(SortableModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'subtitle', 'subsubtitle',
                       'description', 'is_published')
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
            'fields': ('in_navigation', 'template_name', 'menu_title',
                       'meta_title', 'meta_description')
        })
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title', 'subtitle')

    # Django suit
    sortable = 'ordering'


admin.site.register(FlatPage, FlatPageAdmin)