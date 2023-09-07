# forms.py
from datetime import datetime

from django import forms


class LienFacebookForm(forms.Form):
    titre = forms.CharField(max_length=255)
    lien = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1000)
    datesaisie = forms.DateField()


class LienTikTokForm(forms.Form):
    titre = forms.CharField(max_length=255)
    lien = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1000)
    datesaisie = forms.DateField()


class LienTwitterForm(forms.Form):
    titre = forms.CharField(max_length=255)
    lien = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1000)
    datesaisie = forms.DateField()


class LienYoutubeForm(forms.Form):
    titre = forms.CharField(max_length=255)
    lien = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1000)
    datesaisie = forms.DateField()
