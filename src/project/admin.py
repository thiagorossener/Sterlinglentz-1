from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Client, Category, Project


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


#@admin.register(Project)
class ProjectAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ["categories"]
    list_filter = ["client", "is_published"]
    list_display = ["name", "is_published"]

admin.site.register(Project, ProjectAdmin)
