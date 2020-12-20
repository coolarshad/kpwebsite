from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page,Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.blocks import StructBlock
from .blocks import *


class HomePage(Page):
    # pass
    logo=RichTextField()

    content_panels=Page.content_panels+[
        FieldPanel('logo', classname="full"),
        InlinePanel('gallery_images',label="Gallery images"),
        
    ]
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['image_list'] = CarouselContent.objects.all()[1:]
        context['first_image']=CarouselContent.objects.all()[:1].get()
        context['visionmission']=VisionMission.objects.latest('vision')
        context['whatwedos']=WhatWeDoPage.objects.all()
        context['productpages']=ProductPage.objects.all()
        context['about']=AboutPage.objects.latest('about_text')
        context['about_review']=AboutReview.objects.all()
        context['client_review']=ClientReview.objects.all()

        return context
   


class CarouselImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class CarouselContent(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    content_panels =Page.content_panels+ [
        ImageChooserPanel('image'),
        FieldPanel('caption',classname="full"),
    ]

class VisionMission(Page):
    vision=RichTextField()
    mission=RichTextField()

    content_panels=Page.content_panels+[
        FieldPanel('vision',classname="full"),
        FieldPanel('mission',classname="full"),
    ]

class AboutPage(Page):
    about_text=models.CharField(max_length=500)
    what_client_say_text=models.CharField(max_length=500)

    content_panels=Page.content_panels+[
        FieldPanel('about_text',classname="full"),
        FieldPanel('what_client_say_text',classname="full"),
       
    ]

class AboutReview(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )
    name=models.CharField(max_length=250)
    position=models.CharField(max_length=200)
    review=models.CharField(max_length=250)

    content_panels=Page.content_panels+[
        ImageChooserPanel('image'),
        FieldPanel('name',classname="full"),
        FieldPanel('position'),
        FieldPanel('review',classname="full")
    ]

class ClientReview(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )
    name=models.CharField(max_length=250)
    position=models.CharField(max_length=200)
    review=models.CharField(max_length=250)

    content_panels=Page.content_panels+[
        ImageChooserPanel('image'),
        FieldPanel('name',classname="full"),
        FieldPanel('position'),
        FieldPanel('review',classname="full")
    ]



class WhatWeDoPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )
    description=RichTextField()

    content_panels=Page.content_panels+[
        ImageChooserPanel('image'),
        FieldPanel('description',classname="full"),
    ]

class ProductPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )

    body = StreamField([
        ('productblock', ProductBlock()),
    ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]
    

