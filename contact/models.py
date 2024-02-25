from django.db import models
from wagtail import blocks

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ContactBlock(blocks.StaticBlock):

    def get_context(self, value, parent_context=None):
        from contact.forms import ContactForm
        context = super().get_context(value, parent_context)
        context['form'] = ContactForm()
        return context

    class Meta:
        icon = 'mail'
        label = 'Contact'
        admin_text = 'Contact form'
        template = 'contact/blocks/contact_block.html'