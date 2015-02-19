""" Custom toolbar to add custom page model editing. """

from django.utils.translation import ugettext_lazy as _

from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool

from .models import CustomCMSPage


@toolbar_pool.register
class IconExtensionToolbar(ExtensionToolbar):

    """ Provide a toolbar entry for editing this page. """

    model = CustomCMSPage

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(
                    _('Extra Page Settings'), url=url,
                    disabled=not self.toolbar.edit_mode)
