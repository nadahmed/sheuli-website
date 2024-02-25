from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from django.views import View
from django.urls import reverse

class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = request.META['REMOTE_ADDR']
            obj.save()
            return JsonResponse({'url': reverse('newsletter:success')})
        return JsonResponse({'errors': form.errors}, status=400)
    
class NewsletterSuccessView(View):
    
    def get(self, request):
        return render(request, 'newsletter/success.html')