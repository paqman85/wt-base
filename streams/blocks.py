"""Streamfields live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import StreamField


class HeroSimpleBlock(blocks.StructBlock):
    """Hero Section - Simple Text, Image, optional 2 buttons"""
    section_id= blocks.CharBlock(required=False, help_text="Add your section #id")
    title = blocks.CharBlock(required=True, help_text="Add your title.", )
    text = blocks.TextBlock(required=False, help_text="Add additional text.")
    image = DocumentChooserBlock(required=False, help_text="Please choose an SVG Hero image.")
    button_1_text = blocks.CharBlock(required=False, help_text="Add Button 1 text")
    button_1_link = blocks.URLBlock(required=False, help_text = "Where will button 1 go?")
    button_2_text = blocks.CharBlock(required=False, help_text="Add Button 2 text")
    button_2_link = blocks.URLBlock(required=False, help_text = "Where will button 2 go?")
    


    class Meta:  # noqa
        template = "streams/hero_simple.html"
        icon = "edit"
        label = "Hero - Simple"


class Content2BtnBlock(blocks.StructBlock):
    """Content Section with Button- Title, 2 columns of text and a button """

    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    column1text = blocks.RichTextBlock(required=False, label="Column 1", help_text="Add text for column 1.")
    column2text = blocks.RichTextBlock(required=False, label="Column 2", help_text="Add text for column 2.")
    button_text = blocks.CharBlock(required=False, label="Button Text", help_text="Add Button 1 text")
    button_link = blocks.URLBlock(required=False, help_text = "Where will button 1 go?")

    class Meta: # noqa
        template = "streams/content_2_btn.html"
        icon = "edit"
        label = "Content - 2 Columns With Button"

class Content1Block(blocks.StructBlock):
    """Content Block - Single Column"""

    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    text = blocks.RichTextBlock(required=False, label="Section Text", help_text="Please add your section text")
    
    class Meta: #noqa
        template = "streams/content_1.html"
        icon = "edit"
        label = "Standard Content block - Single Column"

class Content2Block(blocks.StructBlock):
    """Content Section with Button- Title, 2 columns of text and a button """

    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    column1text = blocks.RichTextBlock(required=False, label="Column 1", help_text="Add text for column 1.")
    column2text = blocks.RichTextBlock(required=False, label="Column 2", help_text="Add text for column 2.")
    class Meta: # noqa
        template = "streams/content_2.html"
        icon = "edit"
        label = "Content - 2 Columns With Button"

class PreTestimonialsBlock(blocks.StructBlock):
    """PreTestimonials - Set up for Testimonials"""

    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    text = blocks.RichTextBlock(required=False, label="Section Text", help_text="Please add your section text")
    
    class Meta: #noqa
        template = "streams/pre_testimonials.html"
        icon = "edit"
        label = "Pre-Testimonials - Single Column"

class TestimonialBlock(blocks.StreamBlock):
    """Testimonials """
    testimonials = blocks.StructBlock([
        ('author', blocks.CharBlock(required=True, label="Author", help_text="Testimonial Author")),
        ('text', blocks.RichTextBlock(required=True, label="Text", help_text="Testimonial Text")),
        ('image', ImageChooserBlock(required=False, help_text="Please select your Testimonial author photo")),
    ])

    class Meta: # noqa
        template = "streams/testimonials.html"
        icon = "user"
        label = "Testimonials"

class ServiceThreeBlock(blocks.StructBlock):
    """Service section with three services"""
    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    text = blocks.RichTextBlock(required=False, label="Section Text", help_text="Please add your section text")
    icon_code_1 = blocks.CharBlock(required=True, label="Icon Code 1", help_text="Add the Font Awesome Code for Service 1")
    service_title_1 = blocks.CharBlock(required=True, label="Service 1 Title", help_text="Add the Title for Service 1")
    service_text_1 = blocks.CharBlock(required=True, label="Service 1 Text", help_text="Add the Text for Service 1")
    icon_code_2 = blocks.CharBlock(required=True, label="Icon Code 2", help_text="Add the Font Awesome Code for Service 2")
    service_title_2 = blocks.CharBlock(required=True, label="Service 2 Title", help_text="Add the Title for Service 2")
    service_text_2 = blocks.CharBlock(required=True, label="Service 2 Text", help_text="Add the Text for Service 2")
    icon_code_3 = blocks.CharBlock(required=True, label="Icon Code 3", help_text="Add the Font Awesome Code for Service 3")
    service_title_3 = blocks.CharBlock(required=True, label="Service 3 Title", help_text="Add the Title for Service 3")
    service_text_3 = blocks.CharBlock(required=True, label="Service 3 Text", help_text="Add the Text for Service 3")

    class Meta: # noqa
        template = "streams/service_3.html"
        icon = "cog"
        label = "Services (3)"

class Cta1Block(blocks.StructBlock):
    """PreTestimonials - Set up for Testimonials"""

    section_id= blocks.CharBlock(required=False, label="Block ID", help_text="Add your section #id")
    title = blocks.CharBlock(required=True, label="Title", help_text="Add your title.", )
    text = blocks.RichTextBlock(required=False, label="Section Text", help_text="Please add your section text")
    callout = blocks.CharBlock(required=False, label="Callout Style", help_text="CTA style")
    btn_url= blocks.URLBlock(required=False, label="Button URL", help_text = "Button url")
    btn_style=blocks.CharBlock(required=False, label="Button Style", help_text="Add Button style code")
    btn_text=blocks.CharBlock(required=False, label="Button Text", help_text="Add Button 1 text")
    
    class Meta: #noqa
        template = "streams/cta_1.html"
        icon = "success"
        label = "CTA - (Light, Dark, Bubble, Block, Mage)"