import pytest
from pytest_stub.toolbox import stub_global
from unittest.mock import MagicMock, patch, Mock
from django.contrib.sites.models import Site


stub_global(
    {
        "common.djangoapps.edxmako.shortcuts": {
            "render_to_response": "[mock]",
        },
        "lms.djangoapps.static_template_view.views": {
            "render": "[mock]",
        },
    }
)


@pytest.fixture
def mock_site():
    site = Site(domain="example.com", name="example.com")
    with patch("edx_info_pages.views.Site.objects.get_current", return_value=site):
        yield site


@pytest.fixture
def mock_info_page():
    mock_info_page = MagicMock()
    mock_info_page.page.slug = "example"
    mock_info_page.site.domain = "example.com"

    queryset_mock = MagicMock()
    queryset_mock.first.return_value = mock_info_page

    with patch("edx_info_pages.views.InfoPage.objects.filter", return_value=queryset_mock):
        yield mock_info_page


@pytest.fixture
def mock_empty_info_page():
    mock_filter = Mock()
    mock_filter.first.return_value = None
    with patch("edx_info_pages.views.InfoPage.objects.filter", return_value=mock_filter):
        yield mock_filter
