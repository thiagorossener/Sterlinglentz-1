""" Custom general model classses. """

from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class CustomCMSPage(PageExtension):

    """ A custom CMS page that adds an image field. """

    image = models.ImageField(upload_to='cms/pages/')


extension_pool.register(CustomCMSPage)
