from django.db import models
from wagtail.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel


class NavBarSection(ClusterableModel):
    """
    Bar section that contains navigation items.

    Attributes:
        hidden_mobile (bool): If True, the navigation section is hidden on mobile devices.
        nav_items (list): A list of navigation items within the section.
        panels (list): Configuration for the Wagtail admin interface panels.
    """

    hidden_mobile = models.BooleanField(default=False)

    header = ParentalKey(
        'home.Header',
        on_delete=models.CASCADE,
        related_name='nav_section',
        blank=False,
        null=True
    )

    panels = [
        InlinePanel("nav_items", label="Nav Bar Items"),
        FieldPanel("hidden_mobile"),
    ]

class NavBarItem(ClusterableModel):
    """
    NavBar item that belongs to a NavBarSection.

    Attributes:
        nav_section (NavBarSection): The navigation section this item belongs to.
        content (str): The content of the navigation item.
    """
    
    nav_section = ParentalKey(
        'home.NavBarSection',
        on_delete=models.CASCADE,
        related_name='nav_items'
    )

    content = models.CharField(max_length=255)