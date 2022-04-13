from django import forms 
from .models import Subscribe
class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# class SubscribeForm(ModelForm):
    # class Meta:
    #     model = Subscribe
    #     fields = ['subs_name','subs_email']