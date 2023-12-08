from django import forms
from .models import Author, Quote, Tag


class AuthorForm(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea, required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description', 'quote', 'tags']
