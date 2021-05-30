from django.views.generic.base import TemplateView

from wagtail_ckeditor import settings


class IndexView(TemplateView):
    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data["ckeditor_config"] = settings.JSON_CONFIG
        return data
