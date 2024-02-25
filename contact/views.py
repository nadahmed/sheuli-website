from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

class ContactView(View):

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = request.META['REMOTE_ADDR']
            obj.save()
            return JsonResponse({'url': reverse('contact:success')})
        return JsonResponse({'errors': form.errors}, status=400)

class ContactSuccessView(View):

    def get(self, request):
        return render(request, 'contact/success.html')