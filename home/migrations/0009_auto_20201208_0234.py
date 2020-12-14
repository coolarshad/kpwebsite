# Generated by Django 3.1.3 on 2020-12-07 20:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201208_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='body',
            field=wagtail.core.fields.StreamField([('productblock', wagtail.core.blocks.StructBlock([('product', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock())]))]),
        ),
    ]