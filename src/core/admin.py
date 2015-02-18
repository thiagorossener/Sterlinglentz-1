""" Custom general admin classes. """

from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import CustomCMSPage


class CustomCMSPageAdmin(PageExtensionAdmin):

    """ A custom Django admin field for our custom CMS model. """

    pass


admin.site.register(CustomCMSPage, CustomCMSPageAdmin)
