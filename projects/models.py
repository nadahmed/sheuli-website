from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtailmetadata.models import MetadataPageMixin

class ProjectIndex(MetadataPageMixin, Page):    
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        projects = self.get_children().live().order_by('-first_published_at')
        context['projects'] = projects.specific()
        return context

class ProjectDetails(MetadataPageMixin, Page):

    parent_page_types = ['projects.ProjectIndex']

    short_description = models.TextField()
    description = RichTextField()
    images =  StreamField([
        ('image', ImageChooserBlock()),
    ],  use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('images'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # get 4 random related projects excluding self
        projects = ProjectDetails.objects.live().exclude(id=self.id).order_by('?')[:4]
        context['related'] = projects.specific()
        return context