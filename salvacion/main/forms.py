from django import forms

from main.models import Feedback


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'contact__form-input',
                'placeholder': 'Enter Your Name',
                'id': 'name'
            }
        )
    )
    number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'contact__form-input ',
                'placeholder': 'Enter Your Number',
                'id': 'number'
            }
        ),
    )
    message = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'contact__form-input',
                'placeholder': 'Enter Your Message',
                'id': 'message',
                'cols': '30',
                'rows': '10'
            }
        )
    )
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'message']
