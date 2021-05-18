from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtailyoast.edit_handlers import YoastPanel

from streams import blocks


class FlexPage(Page):
    template = "flex/flex_page.html"

    
   

    content = StreamField(
        [
            ("hero_simple", blocks.HeroSimpleBlock()),
            ("content_1", blocks.Content1Block()),
            ("content_2", blocks.Content2Block()),
            ("content_2_btn", blocks.Content2BtnBlock()),
            ("pre_testimonials", blocks.PreTestimonialsBlock()),
            ("testimonials", blocks.TestimonialBlock()),
            ("service_3", blocks.ServiceThreeBlock()),
            ("cta_1", blocks.Cta1Block()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    keywords = models.CharField(default='', blank=True, max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promotion')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])
    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
