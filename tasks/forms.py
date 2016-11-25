from django import forms
from django.utils.translation import ugettext_lazy as _
from tasks.models import task

class taskForm(forms.ModelForm):
    priority_choises = (
    (1, _("Low")),
    (2, _("Medium")),
    (3, _("High")),
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) , required=True, label=_("task subject"))
    priority= forms.ChoiceField(choices=priority_choises , widget=forms.Select(attrs={'class':'form-control'}) , required=True , label=_("progress"))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}), required=True, label=_("task"))
    progress= forms.CharField(widget=forms.TextInput(attrs={'type' : 'number','class' : 'form-control'}) , required=True , label = _("progress"))
    projid  = forms.CharField(widget=forms.TextInput(attrs={'type' : 'hidden'} ), required=False)
    class Meta:
        model = task
        fields= ['subject' , 'priority' , 'content' , 'progress' , 'projid']
