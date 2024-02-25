from wagtailmetadata.models import MetadataPageMixin
from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from wagtail import blocks
from website.blocks import WebsiteBlockField

class HomePage(MetadataPageMixin ,Page):

    body = WebsiteBlockField([], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

@register_setting
class GenericSettings(BaseGenericSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    company_phone = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    working_hours = models.CharField(max_length=255, blank=True, null=True)

    get_quote_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

@register_setting
class SocialMediaSettings(BaseGenericSetting):
    items = StreamField([
        ('social_media', blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('url', blocks.URLBlock(required=True)),
            ('icon', blocks.CharBlock(required=True)),
        ]))
    ], null=True, blank=True, use_json_field=True)

@register_setting
class ReCaptchaSetting(BaseGenericSetting):
    RECAPTCHA_PUBLIC_KEY = models.CharField(max_length=255, blank=True, null=True)
    RECAPTCHA_PRIVATE_KEY = models.CharField(max_length=255, blank=True, null=True)
