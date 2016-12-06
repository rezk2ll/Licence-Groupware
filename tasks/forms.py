from django import forms
from django.utils.translation import ugettext_lazy as _
from tasks.models import task
from django.contrib.auth.models import User
class taskForm(forms.ModelForm):
    priority_choises = (
    (1, _("Low")),
    (2, _("Medium")),
    (3, _("High")),
    )
    print type(priority_choises)
    userlist= User.objects.all()
    team    = []
    for u in userlist:
        team += [("%s" %u.username , _("%s") % u.username)]
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control select-multiple-field'}) , required=True, label=_("task subject"))
    worker  = forms.MultipleChoiceField(choices=team,widget=forms.CheckboxSelectMultiple(attrs={}) , required=True , label=_("Team"))
    priority= forms.ChoiceField(choices=priority_choises , widget=forms.Select(attrs={'class':'form-control'}) , required=True , label=_("Priority"))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}), required=True, label=_("task"))
    progress= forms.CharField(widget=forms.TextInput(attrs={'type' : 'number','class' : 'form-control'}) , required=True , label = _("progress"))
    projid  = forms.CharField(widget=forms.TextInput(attrs={'type' : 'hidden'} ), required=False)
    class Meta:
        model = task
        fields= ['subject' ,'worker', 'priority' , 'content' , 'progress' , 'projid']
