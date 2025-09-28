from django.db import models
from wagtail.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class Header(ClusterableModel):
    """
    Header model to manage the website's header section.

    Attributes:
        page (ParentalKey): A reference to the HomePage model.
        logo (ForeignKey): A reference to the logo image.
        panels (list): Panels for the Wagtail admin interface.
    """
    
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='header',
        blank=False,
        null=True
    )

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Logo",
    )

    panels = [
        FieldPanel("logo"),
        InlinePanel("nav_section", label="Navigation Bar Section"),
    ]