from django import forms
from fnotes.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry