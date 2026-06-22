from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-input',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'form-input',
        })
    )
    subject = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'placeholder': 'What is this about?',
            'class': 'form-input',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell me about your project or opportunity...',
            'class': 'form-input form-textarea',
            'rows': 5,
        })
    )
