from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(label='search_text', max_length=100)