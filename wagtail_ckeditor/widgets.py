from __future__ import absolute_import, unicode_literals

import json

from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.admin.edit_handlers import RichTextFieldPanel
from wagtail.admin.rich_text.converters.editor_html import EditorHTMLConverter
from wagtail.core.rich_text import features
from wagtail.utils.widgets import WidgetWithScript

from wagtail_ckeditor import settings


class CKEditor(WidgetWithScript, widgets.Textarea):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.features = kwargs.pop("features", None)
        if self.features is None:
            self.features = features.get_default_features()
            self.converter = EditorHTMLConverter()
        else:
            self.converter = EditorHTMLConverter(self.features)

    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, attrs=None):
        if value is None:
            translated_value = None
        else:
            translated_value = self.converter.from_database_format(value)
        return super().render(name, translated_value, attrs)

    def render_js_init(self, editor_id, name, value):

        return "CKEDITOR.replace( '%s', %s);" % (
            editor_id,
            mark_safe(json.dumps(settings.WAGTAIL_CKEDITOR_CONFIG)),
        )

    def value_from_datadict(self, data, files, name):
        original_value = super().value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return self.converter.to_database_format(original_value)
