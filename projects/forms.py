from django import forms
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}) , required=True , label=_("Project name"))
    progress= forms.CharField(widget=forms.TextInput(attrs={'type' : 'hidden' ,'value' : 0,'class' : 'form-control'}) , required=True , label = _("progress"))
    class Meta:
        model = Project
        fields= ['name' , 'progress']
