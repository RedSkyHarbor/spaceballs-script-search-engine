from django import forms

class SearchForm(forms.Form):
    character = forms.CharField(label="Character name", max_length=128, required=False)
    quote = forms.CharField(label="Quote", max_length=1024, required=False)
