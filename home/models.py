from wagtailmetadata.models import MetadataPageMixin

from wagtail.models import Page


class HomePage(MetadataPageMixin ,Page):
    pass
