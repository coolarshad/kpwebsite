from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock

class ProductBlock(blocks.StructBlock):
    product = blocks.CharBlock()
    description=blocks.RichTextBlock()
    product_file=DocumentChooserBlock()
    
    class Meta:
        icon = 'placeholder'
        template = 'home/blocks/detail.html'
