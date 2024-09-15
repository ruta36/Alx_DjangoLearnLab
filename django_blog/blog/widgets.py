from django import forms
from .models import Tag

class TagWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})['placeholder'] = 'Enter tags separated by commas'
        super().__init__(*args, **kwargs)

    def format_value(self, value):
        if value is None:
            return ''
        return ', '.join(tag.name for tag in value.all())
