from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from suit.admin import SortableModelAdmin
from suit.admin import SortableStackedInline

from .models import (Client, Category, Project, ProjectContent,
                     ProjectVideo, ProjectImage)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


""" Polymorphic Admin. """


class ProjectContentChildAdmin(PolymorphicChildModelAdmin):
    """ Child base admin. """
    base_model = ProjectContent


class ProjectVideoAdmin(ProjectContentChildAdmin):
    """ Child concrete admin. """
    pass


class ProjectImageAdmin(ProjectContentChildAdmin):
    """ Child concrete admin. """
    pass


@admin.register(ProjectContent)
class ProjectContentAdmin(PolymorphicParentModelAdmin):
    """ Parent concrete admin. """
    base_model = ProjectContent
    child_models = (
        (ProjectVideo, ProjectVideoAdmin),
        (ProjectImage, ProjectImageAdmin),
    )


class ProjectVideoInline(admin.StackedInline):
    """ Child inline. """
    extra = 0
    model = ProjectVideo
    readonly_fields = ['projectcontent_ptr']


class ProjectImageInline(admin.StackedInline):
    extra = 0
    model = ProjectImage
    readonly_fields = ['projectcontent_ptr']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [ProjectImageInline, ProjectVideoInline]
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
