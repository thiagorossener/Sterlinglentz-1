from django.contrib import admin

from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin

from menu.models import MenuNode


class MenuNodeAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 30
    list_display = ('name', 'url', 'slug')
    sortable = 'ordering'
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(MenuNode, MenuNodeAdmin)
