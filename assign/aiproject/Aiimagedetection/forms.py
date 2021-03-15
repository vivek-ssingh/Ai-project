from django.forms import ModelForm
from .models import *
class ElementsForm(ModelForm):
    class Meta:
        model=Elements
        fields='__all__'
