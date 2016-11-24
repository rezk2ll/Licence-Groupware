from django import forms
from django.utils.translation import ugettext_lazy as _
from messaging.models import Mail

class MessageForm(forms.ModelForm):
    reciver = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}) , required=True , label=_("reciver"))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}) , required=True , label=_("subject"))
    message = forms.CharField(widget=forms.Textarea( attrs={'class' : 'form-control'}) , required=True , label=_("message"))
    class Meta:
        model = Mail
        fields = ['reciver', 'subject', 'message']
