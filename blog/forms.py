from django import forms
from django.utils.translation import ugettext_lazy as _
from blog.models import Post , Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True , label=_("Title"))
    body  = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}) ,required=True , label=_("Post"))
    class Meta:
        model  = Post
        fields = ['title' , 'body']

class CommentForm(forms.ModelForm):
    bodytext = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control' , 'rows':5}) , required=True , max_length=200 , min_length=10)
    class Meta:
        model  = Comment
        fields = ['bodytext']
