import pytest
from unittest.mock import patch
from django.http import HttpRequest

from ..views import info_page_render


def test_info_page_render_with_page(mock_site, mock_info_page):
    """
    Check when the InfoPage exists.
    """

    request = HttpRequest()

    with patch("edx_info_pages.views.render_to_response") as mock_render_to_response:
        info_page_render(request, "example_template.html")

    mock_render_to_response.assert_called_once_with(
        "edx_info_pages/infopage.html", {"page": mock_info_page}
    )


def test_info_page_render_without_page(mock_site, mock_empty_info_page):
    """
    Check when the InfoPage does not exist.
    """

    request = HttpRequest()
    template = "example_template.html"

    with patch("edx_info_pages.views.render") as mock_render:
        info_page_render(request, template)

    mock_render.assert_called_once_with(request, template)


def test_info_page_render_exception(mock_site):
    """
    Check when an exception occurs while retrieving the InfoPage.
    """

    with patch(
        "edx_info_pages.views.InfoPage.objects.filter",
        side_effect=Exception("Unexpected error"),
    ):
        request = HttpRequest()

        with pytest.raises(Exception) as exc_info:
            info_page_render(request, "example_template.html")

    assert str(exc_info.value) == "Unexpected error"
