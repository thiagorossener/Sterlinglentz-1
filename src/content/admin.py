from django.contrib import admin

from .models import Block, Template
from .forms import BlockAdminForm


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    form = BlockAdminForm
    fieldsets = (
        (None, {
            'fields': ('identifier', 'description', 'is_published')
        }),
        (None, {
            'fields': ('content', )
        }),
    )


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass
