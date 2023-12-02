
Edx Info Pages
-----

----
**Description**

-----
This django application extends OpenEdx LMS staff functionality. It adds extra tab in lms admin panel `Info Pages`
where staff can create info page for different languages.
---
**Installation**

---

```angular2html
sudo -sHu edxapp
cd ~
. edxapp_env
pip install git+git@gitlab.raccoongang.com:kraken/icnc-lilac/edx-info-pages.git#egg=edx-info-pages
cd edx-platform
paver update_db
exit
sudo /edx/bin/supervisorctl restart edxapp:lms
```
---
**Configuration**

---
All plugin's settings located in `edx_info_pages/settings/common.py` 
- Make sure to setup `MODELTRANSLATION_LANGUAGES`. This is a tuple of supported
languages. In case it's not configured the default option will be default platform
  language from `LANGUAGE_CODE`
- `MODELTRANSLATION_DEFAULT_LANGUAGE` language for info page translation.
Default value is `LANGUAGE_CODE`.
- To modify TinyMCE config you can update `TINYMCE_DEFAULT_CONFIG`.

## Local development

### Devbox

#### Prerequisites
Installed https://devbox.sh/

Open development environment: 
```
devbox shell
```

Build requirements w/o opening dev env: 
```
devbox run requirements
```

Run tests w/o opening dev env: 
```
devbox run tests
```
