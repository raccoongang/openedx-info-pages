from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField


class InfoPage(models.Model):
    ABOUT = 'about'
    CONTACT = 'contact'
    FAQ = 'faq'
    HELP = 'help'
    TOS = 'tos'
    HONOR = 'honor'
    TOS_AND_HONOR = 'tos_and_honor'
    PRIVACY = 'privacy'
    PRESS = 'press'
    BLOG = 'blog'
    DONATE = 'donate'

    PAGES = (
        (ABOUT, _('About')),
        (CONTACT, _('Contact')),
        (FAQ, _('FAQ')),
        (HELP, _('Help')),
        (TOS, _('TOS')),
        (HONOR, _('Honor')),
        (TOS_AND_HONOR, _('TOS and honor')),
        (PRIVACY, _('Privacy')),
        (PRESS, _('Press')),
        (BLOG, _('Blog')),
        (DONATE, _('Donate')),
    )

    page = models.CharField(max_length=50, choices=PAGES)
    site = models.ForeignKey(
        Site,
        default=settings.SITE_ID,
        related_name="info_pages",
        help_text=_(
            'The Site that this provider configuration belongs to.'
        ),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    text = HTMLField()

    class Meta:
        unique_together = ["page", "site"]

    def __str__(self):
        return f'{self.page}'

    def site_display_name(self):
        return self.site and self.site.name or None

