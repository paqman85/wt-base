"""Streamfields live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock



class HeroSimpleBlock(blocks.StructBlock):
    """Hero Section - Simple Text, Image, optional 2 buttons"""
    section_id= blocks.CharBlock(required=False, help_text="Add your section #id")
    title = blocks.CharBlock(required=True, help_text="Add your title.", )
    text = blocks.TextBlock(required=False, help_text="Add additional text.")
    image = ImageChooserBlock(required=False, help_text="Please choose a Hero image.")
    button_1_text = blocks.CharBlock(required=False, help_text="Add Button 1 text")
    button_1_link = blocks.URLBlock(required=False, help_text = "Where will button 1 go?")
    button_2_text = blocks.CharBlock(required=False, help_text="Add Button 2 text")
    button_2_link = blocks.URLBlock(required=False, help_text = "Where will button 2 go?")
    


    class Meta:  # noqa
        template = "streams/hero_simple.html"
        icon = "edit"
        label = "Hero - Simple"