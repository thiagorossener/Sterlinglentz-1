from django.views.generic.base import ContextMixin

from .models import Block


class BlockMixin(ContextMixin):

    """ """

    block_identifier = None

    def get_context_data(self, **kwargs):
        """ Add the extra JSON data to the context. """
        context = super(BlockMixin, self).get_context_data(**kwargs)
        context.update(self.get_block().json)
        return context

    def get_block(self):
        """ Get or create the Block instance. """
        block = None
        block, created = Block.objects.get_or_create(
            identifier=self.get_block_identifier())
        return block

    def get_block_identifier(self):
        """ Return the identifier as defined by the implementing view. """
        return self.block_identifier
