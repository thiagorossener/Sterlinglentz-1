""" A custom django-cms app hook to allow functionality for projects. """

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ProjectAppHook(CMSApp):

    """ An app that allows listing of projects and project detail pages. """

    name = _("Project Apphook")
    urls = ["project.urls"]
    app_name = "projects"


apphook_pool.register(ProjectAppHook)
