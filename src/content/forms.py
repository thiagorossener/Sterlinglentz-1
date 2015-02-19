from django import forms

from .models import Block

DOT_SEPARATED_STRING_REGEX = r"^[\w.]+[\w]+$"


class BlockAdminForm(forms.ModelForm):

    """ A form to be used by the admin to add custom admin editing feature. """

    identifier = forms.RegexField(
        regex=DOT_SEPARATED_STRING_REGEX,
        error_message="""Enter a dot-separated string only""")

    class Meta:
        model = Block
