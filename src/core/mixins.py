from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse


class AjaxPartialRenderingMixin(object):

    """ """

    partial_template_name = None

    def get_template_names(self):
        """ Insert the partial template name. """
        template_names = super(AjaxPartialRenderingMixin, self) \
            .get_template_names()
        if self.request.is_ajax():
            if self.partial_template_name is None:
                raise ImproperlyConfigured("AjaxPartialRenderingMixin requires"
                    " the definition of a 'partial_template_name' variable")
            template_names = [self.partial_template_name, ] + template_names
        return template_names

    def render_to_response(self, context, **response_kwargs):
        """ Return a JSON response for future features. """
        response = super(AjaxPartialRenderingMixin, self).render_to_response(
            context, **response_kwargs)
        if self.request.is_ajax():
            content = response.render().content
            return JsonResponse({
                'content': content
            })
        return response
