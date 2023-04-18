from django.forms import ModelForm, TextInput, Textarea, EmailInput

from portfolio.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'message': Textarea(
                attrs={
                    'name': '',
                    'id': 'message',
                    'cols': '30',
                    'rows': '7',
                    'class': 'form-control',
                    'placeholder': 'Message'
                }
            )
        }
