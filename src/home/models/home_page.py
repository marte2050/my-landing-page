from wagtail.admin.panels import InlinePanel

from wagtail.models import Page


class HomePage(Page):
    """
    HomePage model representing the main page of the website.

    Attributes:
        content_panels (list): A list of panels for Wagtail admin interface.
    """
    
    content_panels = Page.content_panels + [
        InlinePanel("sections", label="Sections"),
        InlinePanel("header", label="Header", max_num=1),
    ]
