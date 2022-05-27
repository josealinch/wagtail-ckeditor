from __future__ import absolute_import, unicode_literals

from django.forms import Media, widgets
from wagtail.utils.widgets import WidgetWithScript


class CKEditor(WidgetWithScript, widgets.Textarea):
    def render_js_init(self, id_, name, value):
        return "ClassicEditor.create(document.getElementById('{id}'))".format(
            id=id_
        )

    @property
    def media(self):
        return Media(js=["wagtail_ckeditor/ckeditor.js"])
