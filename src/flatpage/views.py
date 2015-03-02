from django.http import Http404
from django.views.generic import DetailView

from flatpage.models import FlatPage
from core.mixins import AjaxPartialRenderingMixin


class FlatpageView(AjaxPartialRenderingMixin, DetailView):
    template_name = 'flatpage/basic.html'
    context_object_name = 'flatpage'

    def get_object(self, queryset=None):
        url = self.kwargs['url']
        if not url.startswith('/'):
            url = '/' + url
        try:
            flatpage = FlatPage.objects.get(url__exact=url)
        except FlatPage.DoesNotExist:
            raise Http404
        return flatpage

    def get_template_names(self):
        if self.object.template_name:
            return [self.object.template_name, ]
        return [self.template_name, ]
