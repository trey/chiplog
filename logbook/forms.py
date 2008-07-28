from logbook.models import Entry
from django import forms

class LogForm(forms.ModelForm):
    class Meta:
        model=Entry
