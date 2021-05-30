# Wagtail CKEditor plugin

This is a [Wagtail](https://wagtail.io/) plugin, which allows [CKEditor](http://ckeditor.com/) to be used as an internal editor
instead of hallo.js or draftail.

## Requirments

Wagtail 2+
Django 3+

## How to install

Include `wagtail_ckeditor` in your `INSTALLED_APPS`.

Ensure that you have this entry in your `settings.py` file.

.. code-block:: python

    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtail_ckeditor.widgets.CKEditor'
        }
    }

There are several options you can add to your `settings.py` file.

- CKEditor settings, defaults to:
  WAGTAIL_CKEDITOR_CONFIG = getattr(settings, 'WAGTAIL_CKEDITOR_CONFIG',
  {'language': settings.LANGUAGE_CODE,
  'skin': 'moono-dark',
  'toolbar': [
  {'name': 'basicstyles',
  'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript']},
  {'name': 'clipboard',
  'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo',
  'Redo']},
  {'name': 'paragraph',
  'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
  'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
  {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
  '/',
  {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
  {'name': 'insert',
  'items': ['Image', 'Mathjax' if WAGTAIL_CKEDITOR_USE_MATH else '-', 'Table',
  'HorizontalRule', 'SpecialChar']},
  {'name': 'colors', 'items': ['TextColor', 'BGColor']},
  {'name': 'document', 'items': ['Maximize', '-', 'Source']},
  ]
  })
  Inspired by:

---

Richard Mitchell (https://github.com/isotoma/wagtailtinymce.git)
mastnym (https://github.com/mastnym/wagtail-ckeditor)
