from django.urls import include, path
from lms.djangoapps.static_template_view.urls import urlpatterns as patterns
from .views import info_page_render


for url in patterns:
    if url.callback.__name__ == 'render':
        url.callback = info_page_render

urlpatterns = [
    path('tinymce/', include('tinymce.urls'))
]
