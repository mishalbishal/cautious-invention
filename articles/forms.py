from django import forms
from django.utils.translation import gettext_lazy as _

from django_comments_xtd import forms as forms_xtd


class EmailOptionalForm(forms_xtd.XtdCommentForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override email field to be optional
        self.fields['email'].required = False
