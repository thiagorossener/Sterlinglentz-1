import os

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse


class AjaxPartialRenderingMixin(object):

    """ """

    def get_partial_template_names(self):
        partial_template_names = []
        for template_name in self.get_template_names():
            name, ext = os.path.splitext(template_name)
            partial_template_names.append("{}--partial{}".format(name, ext))
        return partial_template_names

    def render_to_response(self, context, **response_kwargs):
        """ Return a JSON response for future features. """
        response_kwargs.setdefault('content_type', self.content_type)
        template_names = []
        if self.request.is_ajax():
            template_names = self.get_partial_template_names()
        else:
            template_names = self.get_template_names()
        response = self.response_class(
            request=self.request,
            template=template_names,
            context=context,
            **response_kwargs
        )
        if self.request.is_ajax():
            content = response.render().content
            return JsonResponse({
                'content': content
            })
        return response
