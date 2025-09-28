from django.db import models
from wagtail.models import Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel

class Section(Orderable):
    """
    A section model representing a section of a webpage.

    Attributes:
        title_page (str): The title of the section.
        sub_title (str): The subtitle of the section.
        content (str): The main content of the section.
        panels (list): A list of FieldPanel instances for Wagtail admin interface.
    """

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='sections'
    )

    title_page = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel('title_page'),
        FieldPanel('sub_title'),
        FieldPanel('content'),
    ]