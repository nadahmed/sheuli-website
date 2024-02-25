from django.urls import path
from .views import NewsletterView, NewsletterSuccessView

app_name = 'newsletter'

urlpatterns = [
    path('', NewsletterView.as_view(), name='index'),
    path('success/', NewsletterSuccessView.as_view(), name='success'),
]
