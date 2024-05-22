from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from django.views import View
from django.urls import reverse
from home.models import ReCaptchaSetting
import requests

def valid_captcha(request):
    settings = ReCaptchaSetting.load()

    data = request.POST
    if not settings.enabled:
        return True
    token = data.getlist('g-recaptcha-response')
    if not token or token == '' or "".join(token).strip() == '':
        return False
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': token
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result['success']

class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)
        if not valid_captcha(request):
            return JsonResponse({'errors': {'email': ['Invalid captcha. Please refresh page.']}}, status=400)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = request.META['REMOTE_ADDR']
            obj.save()
            return JsonResponse({'url': reverse('newsletter:success')})
        return JsonResponse({'errors': form.errors}, status=400)
    
class NewsletterSuccessView(View):
    
    def get(self, request):
        return render(request, 'newsletter/success.html')