from django.forms import ModelForm
from .models import Beaco


class BeacoForm(ModelForm):
    class Meta:
        model = Beaco
        fields = ['title', 'memo', 'important']


