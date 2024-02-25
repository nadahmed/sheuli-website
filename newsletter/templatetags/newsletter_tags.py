from django import template

register = template.Library()

@register.simple_tag()
def newsletter_form():
    from newsletter.forms import NewsletterForm
    return NewsletterForm()