# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from openedx.core.djangoapps.plugins.constants import ProjectType, PluginSettings, PluginURLs, SettingsType


class EdxInfoPagesConfig(AppConfig):
    name = 'edx_info_pages'
    verbose_name = "Edx info pages"

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'edx_info_pages',
                PluginURLs.APP_NAME: 'edx_info_pages',
                PluginURLs.REGEX: '',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        }
    }
