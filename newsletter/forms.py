from django.forms import ModelForm, EmailInput
from .models import Newsletter
from home.models import ReCaptchaSetting
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class NewsletterForm(ModelForm):
            
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
        }