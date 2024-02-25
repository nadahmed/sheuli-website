from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from projects.models import  ProjectDetails
from wagtail.fields import StreamField

class TestimonialBlock(blocks.StructBlock):
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('quote', blocks.TextBlock(required=True)),
            ('name', blocks.CharBlock(required=True)),
            ('position', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
        ]))
    
    class Meta:
        template = 'blocks/testimonial_block.html'
        icon = 'group'
        label = 'Testimonial Block'

class TeamBlock(blocks.StructBlock):
    sub_title = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=True)
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('position', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
            ('socials', blocks.ListBlock(
                blocks.StructBlock([
                    ('name', blocks.CharBlock(required=True)),
                    ('url', blocks.URLBlock(required=True)),
                    ('icon', blocks.CharBlock(required=True, help_text='Font Awesome 5 icon')),
                ])
            )),
          ]))
    
    class Meta:
        template = 'blocks/team_block.html'
        icon = 'group'
        label = 'Team Block'

class FactBlock(blocks.StructBlock):
    items = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('number', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
        ]), min_num=4, max_num=4)

    class Meta:
        template = 'blocks/fact_block.html'
        icon = 'image'
        label = 'Fact Block'

class FAQListBlock(blocks.StructBlock):
    faqs = blocks.ListBlock(
        blocks.StructBlock([
            ('question', blocks.CharBlock(required=True)),
            ('answer', blocks.TextBlock(required=True)),
        ]), min_num=2
    )

    class Meta:
        template = 'blocks/faq_block.html'
        icon = 'help'
        label = 'FAQ'

class VideoBlock(blocks.StructBlock):
    video_url = blocks.URLBlock(required=True)

    # Convert youtube url to embed url
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['video_url'] = value['video_url'].replace('watch?v=', 'embed/')
        return context

    class Meta:
        template = 'blocks/video_block.html'
        icon = 'media'
        label = 'Video'

class ProjectListBlock(blocks.StaticBlock):

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        # Get 6 latest projects based on current language without duplicates
        projects = ProjectDetails.objects.live().order_by('-first_published_at')[:3]
        context['projects'] = projects
        return context

    class Meta:
        template = 'blocks/project_list_block.html'
        icon = 'folder-open-inverse'
        label = 'Project List'
        admin_text = 'List of projects'

class FeatureBlock(blocks.StructBlock):

    class FeatureItemBlock(blocks.StructBlock):
        title = blocks.CharBlock(required=True)
        description = blocks.TextBlock(required=True)
        image = ImageChooserBlock(required=True)
    
    items = blocks.ListBlock(FeatureItemBlock(), max_num=4)

    class Meta:
        template = 'blocks/feature_block.html'
        icon = 'image'
        label = 'Feature Block'

class HeroCaraouselBlock(blocks.StructBlock):
    
    class HeroItemBlock(blocks.StructBlock):
        title = blocks.CharBlock(required=False)
        sub_title = blocks.TextBlock(required=False)
        button_text = blocks.CharBlock(required=False)
        button_link = blocks.PageChooserBlock(required=False)
        background_image = ImageChooserBlock(required=True)

    items = blocks.ListBlock(HeroItemBlock)

    class Meta:
        template = 'blocks/hero_caraousel_block.html'
        icon = 'image'
        label = 'Hero Caraousel Block'

class AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    sub_title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True)
    button_text = blocks.CharBlock(required=False, default='Learn More')
    button_link = blocks.PageChooserBlock(required=False)
    image = ImageChooserBlock(required=True)
    image_position = blocks.ChoiceBlock(choices=[
        ('left', 'Left'),
        ('right', 'Right'),
    ], default='left')

    class Meta:
        template = 'blocks/about_block.html'
        icon = 'image'
        label = 'About Block'

class WebsiteBlockField(StreamField):
    
    def __init__(self, block_types, use_json_field=None, **kwargs):
        block_types.extend([
            ('hero_caraousel', HeroCaraouselBlock()),
            ('feature', FeatureBlock()),
            ('about', AboutBlock()),
            ('project_list', ProjectListBlock()),
            ('video', VideoBlock()),
            ('faq', FAQListBlock()),
            ('fact', FactBlock()),
            ('team', TeamBlock()),
            ('testimonial', TestimonialBlock()),
        ])
        super().__init__(block_types, use_json_field, **kwargs)
