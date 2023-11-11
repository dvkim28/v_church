from django.utils import timezone

from django import forms

from main.models import Feedback


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ))
    number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    message = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'message']
