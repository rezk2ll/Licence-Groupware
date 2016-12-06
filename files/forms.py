from django import forms
from django.utils.translation import ugettext_lazy as _
from files.models import Filemodel
from groupware.settings import UPLOAD_DIR

class FileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) ,required=True , label=_("Description :"))
    filedata    = forms.FileField()
    class Meta:
        model  = Filemodel
        fields = ['description' , 'filedata']
