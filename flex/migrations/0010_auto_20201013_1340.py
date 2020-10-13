# Generated by Django 3.1.2 on 2020-10-13 17:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0009_auto_20201013_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('hero_simple', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text.', required=False)), ('image', wagtail.documents.blocks.DocumentChooserBlock(help_text='Please choose an SVG Hero image.', required=False)), ('button_1_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text', required=False)), ('button_1_link', wagtail.core.blocks.URLBlock(help_text='Where will button 1 go?', required=False)), ('button_2_text', wagtail.core.blocks.CharBlock(help_text='Add Button 2 text', required=False)), ('button_2_link', wagtail.core.blocks.URLBlock(help_text='Where will button 2 go?', required=False))])), ('content_1', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', label='Block ID', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', label='Title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Please add your section text', label='Section Text', required=False))])), ('content_2', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', label='Block ID', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', label='Title', required=True)), ('column1text', wagtail.core.blocks.RichTextBlock(help_text='Add text for column 1.', label='Column 1', required=False)), ('column2text', wagtail.core.blocks.RichTextBlock(help_text='Add text for column 2.', label='Column 2', required=False))])), ('content_2_btn', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', label='Block ID', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', label='Title', required=True)), ('column1text', wagtail.core.blocks.RichTextBlock(help_text='Add text for column 1.', label='Column 1', required=False)), ('column2text', wagtail.core.blocks.RichTextBlock(help_text='Add text for column 2.', label='Column 2', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Add Button 1 text', label='Button Text', required=False)), ('button_link', wagtail.core.blocks.URLBlock(help_text='Where will button 1 go?', required=False))])), ('pre_testimonials', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', label='Block ID', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', label='Title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Please add your section text', label='Section Text', required=False))])), ('testimonials', wagtail.core.blocks.StreamBlock([('testimonials', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.CharBlock(help_text='Testimonial Author', label='Author', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Testimonial Text', label='Text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please select your Testimonial author photo', required=False))]))])), ('service_3', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Add your section #id', label='Block ID', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Add your title.', label='Title', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Please add your section text', label='Section Text', required=False)), ('icon_code_1', wagtail.core.blocks.CharBlock(help_text='Add the Font Awesome Code for Service 1', label='Icon Code 1', required=True)), ('service_title_1', wagtail.core.blocks.CharBlock(help_text='Add the Title for Service 1', label='Service 1 Title', required=True)), ('service_text_1', wagtail.core.blocks.CharBlock(help_text='Add the Text for Service 1', label='Service 1 Text', required=True)), ('icon_code_2', wagtail.core.blocks.CharBlock(help_text='Add the Font Awesome Code for Service 2', label='Icon Code 2', required=True)), ('service_title_2', wagtail.core.blocks.CharBlock(help_text='Add the Title for Service 2', label='Service 2 Title', required=True)), ('service_text_2', wagtail.core.blocks.CharBlock(help_text='Add the Text for Service 2', label='Service 2 Text', required=True)), ('icon_code_3', wagtail.core.blocks.CharBlock(help_text='Add the Font Awesome Code for Service 3', label='Icon Code 3', required=True)), ('service_title_3', wagtail.core.blocks.CharBlock(help_text='Add the Title for Service 3', label='Service 3 Title', required=True)), ('service_text_3', wagtail.core.blocks.CharBlock(help_text='Add the Text for Service 3', label='Service 3 Text', required=True))]))], blank=True, null=True),
        ),
    ]
