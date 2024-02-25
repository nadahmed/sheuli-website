from django.forms import ModelForm, EmailInput
from .models import Newsletter
from home.models import ReCaptchaSetting
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class NewsletterForm(ModelForm):

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
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
        }