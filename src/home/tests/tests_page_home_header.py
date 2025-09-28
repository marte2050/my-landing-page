from wagtail.test.utils import WagtailPageTestCase
from bs4 import BeautifulSoup, Tag
from wagtail.models import Page, Site
from home.models import (
    HomePage,
    Header,
    NavBarSection,
    NavBarItem,
)


class MyPageTest(WagtailPageTestCase):
    @classmethod
    def setUpTestData(cls):
        root = Page.get_first_root_node()
        cls.home = HomePage(title="Home")
        root.add_child(instance=cls.home)
        cls.home.save_revision().publish()

        header = Header.objects.create(page=cls.home)
        navsection = NavBarSection.objects.create(header=header)
        NavBarItem.objects.create(nav_section=navsection, content="home")
        NavBarItem.objects.create(nav_section=navsection, content="contact")

        Site.objects.create(
            hostname="testserver",
            root_page=root,
            is_default_site=True,
            site_name="testserver",
        )

    def test_home_page_header_hierarchy(self):
        response = self.client.get(self.home.url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        header = soup.find("my-header")
        assert header is not None

        navbar = header.find("my-navbar")
        assert navbar is not None

        navsections = navbar.find_all("my-navbarsection")
        assert navsections is not None
        assert len(navsections) == 2

        navesection01: Tag = navsections[0]
        navitems_section01 = navesection01.find_all("my-navbaritem")
        assert len(navitems_section01) == 1

        navesection02: Tag = navsections[1]
        navitems_section02 = navesection02.find_all("my-navbaritem")
        assert len(navitems_section02) == 2