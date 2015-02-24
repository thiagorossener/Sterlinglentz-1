from django.contrib import admin

from .models import Snippet
from .forms import SnippetForm


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    form = SnippetForm
