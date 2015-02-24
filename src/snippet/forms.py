from django import forms

from .models import Snippet

DOT_SEPARATED_STRING_REGEX = r"^[\w.]+[\w]+$"


class SnippetForm(forms.ModelForm):

    """"""

    slug = forms.RegexField(
        regex=DOT_SEPARATED_STRING_REGEX,
        error_message="""Enter a dot-separated string only""")

    class Meta:
        model = Snippet
