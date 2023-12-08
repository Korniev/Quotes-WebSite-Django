# forms.py
from .models import Author, Quote
from django import forms


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author']

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        authors_choices = kwargs.pop('authors_choices', [])
        self.fields['author'].queryset = Author.objects.filter(id__in=[a[0] for a in authors_choices])
