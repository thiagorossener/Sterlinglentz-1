""" Custom views for the project app hook. """
from itertools import izip_longest

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from project.models import Project, ProjectImage, ProjectVideo
from core.mixins import AjaxPartialRenderingMixin


class ProjectListView(AjaxPartialRenderingMixin, ListView):

    """ A custom list view for django cms project app hook. """

    template_name = "project/list.html"
    model = Project
    context_object_name = "projects"
    group_size = 3

    def get_queryset(self):
        """ Only return published projects. """
        projects = Project.published.all()
        return projects

    def chunks(self, l, n):
        for i in xrange(0, len(l), n):
            yield l[i:i+n]

    def get_context_data(self, **kwargs):
        """ Group projects into rows of three. """
        c = super(ProjectListView, self).get_context_data(**kwargs)
        c['projects'] = list(self.chunks(c['projects'], self.group_size))
        return c


class ProjectDetailView(AjaxPartialRenderingMixin, DetailView):

    """ A custom detail view for django cms project app hook. """

    template_name = "project/detail.html"
    model = Project
    context_object_name = "project"

    def order_media(self, media_items):
        """ Partition images into landscape/portrait and order.

        """
        rows = []
        media_items = list(media_items)
        for i, item in enumerate(media_items):
            if isinstance(item, ProjectImage):
                if item.is_landscape():
                    rows.append([item, ])
                else:
                    # Go fish for another portrait if possible
                    cols = [item, ]
                    try:
                        remaining = media_items[i+1:]
                    except:
                        remaining = []
                    for j, subitem in enumerate(remaining):
                        if isinstance(subitem, ProjectImage) and subitem.is_portrait():
                            cols.append(media_items.pop(i + j + 1))
                            break
                    rows.append(cols)
            else:
                rows.append([item, ])
        return rows

    def get_context_data(self, **kwargs):
        """ Group projects into rows of three. """
        c = super(ProjectDetailView, self).get_context_data(**kwargs)
        c['media_items'] = self.order_media(self.object.content_items.all())
        return c

    def get_queryset(self):
        """ More efficiently fetch the project object. """
        return super(ProjectDetailView, self).get_queryset() \
            .prefetch_related("categories").select_related("client")
