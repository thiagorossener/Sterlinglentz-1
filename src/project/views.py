""" Custom views for the project app hook. """

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Project


class ProjectListView(ListView):

    """ A custom list view for django cms project app hook. """

    template_name = "cms/apps/project/list.html"
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        """ Only return published projects. """
        return Project.published.all()


class ProjectDetailView(DetailView):

    """ A custom detail view for django cms project app hook. """

    template_name = "cms/apps/project/detail.html"
    model = Project
    context_object_name = "project"
