# importing forms
from django import forms


# creating our forms
class SignupForm(forms.Form):
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    twitterID = forms.CharField(label='Put twitter ID', max_length=100)

class texts(forms.Form):
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    sentence = forms.CharField(label='Put a text', max_length=300)


class status(forms.Form):
    identity_hate = forms.IntegerField()
    obscene = forms.IntegerField()
    threat = forms.IntegerField()
    insult = forms.IntegerField()
    severe_toxic = forms.IntegerField()
    toxic = forms.IntegerField()