# forms.py
from .models import Author, Quote
from django import forms


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):

    tags = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    def __init__(self, *args, **kwargs):
        authors_choices = kwargs.pop('authors_choices', [])
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['author'].choices = authors_choices