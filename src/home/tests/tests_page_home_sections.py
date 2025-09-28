from wagtail.test.utils import WagtailPageTestCase
from bs4 import BeautifulSoup
from wagtail.models import Page, Site
from home.models import (
    HomePage,
    Section
)


class PageHomeSectionTest(WagtailPageTestCase):
    @classmethod
    def setUpTestData(cls):
        root = Page.get_first_root_node()
        cls.home = HomePage(title="Home")
        root.add_child(instance=cls.home)
        cls.home.save_revision().publish()

        Section.objects.create(
            page=cls.home,
            title_page="Title Page",
            sub_title="Sub Title",
            content="This is the content of the section."
        )

        Site.objects.create(
            hostname="testserver",
            root_page=root,
            is_default_site=True,
            site_name="testserver",
        )

    def test_home_page_section_hierarchy(self):
        response = self.client.get(self.home.url)
        soup = BeautifulSoup(response.content, "html.parser")
        section = soup.find("my-section")
        assert section is not None