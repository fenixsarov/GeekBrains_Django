from django import forms
from .models import Unit

class UnitsForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('__all__')