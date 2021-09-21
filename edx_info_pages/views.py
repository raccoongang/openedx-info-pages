import logging

from common.djangoapps.edxmako.shortcuts import render_to_response
from django.contrib.sites.models import Site
from edx_info_pages.models import InfoPage
from lms.djangoapps.static_template_view.views import render


log = logging.getLogger(__name__)


def info_page_render(request, template):
    current_site = Site.objects.get_current(request)
    page_name = template.split('.')[0]

    page = InfoPage.objects.filter(
        page=page_name,
        site=current_site
    ).first()

    if page:
        return render_to_response('edx_info_pages/infopage.html', {'page': page})

    return render(request, template)

