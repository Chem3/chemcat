from django import forms

from .models import Chemicals, Bottles

class SearchForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('query')