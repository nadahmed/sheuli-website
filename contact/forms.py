from django.forms import ModelForm
from .models import Contact
from django import forms
from home.models import ReCaptchaSetting
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = ReCaptchaSetting.load()
        if settings.RECAPTCHA_PUBLIC_KEY and settings.RECAPTCHA_PRIVATE_KEY:
            self.fields['captcha'] = ReCaptchaField(
                label='',
                public_key=settings.RECAPTCHA_PUBLIC_KEY,
                private_key=settings.RECAPTCHA_PRIVATE_KEY,
                widget=ReCaptchaV2Invisible(attrs={'class': 'form-control pt-4'})
            )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }
