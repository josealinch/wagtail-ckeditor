import json

from django.conf import settings

WAGTAIL_CKEDITOR_CONFIG = getattr(
    settings,
    "WAGTAIL_CKEDITOR_CONFIG",
    {
        "language": "en",
        "skin": "moono-dark",
        "toolbar": [
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {
                "name": "insert",
                "items": ["Image", "Table", "HorizontalRule", "SpecialChar"],
            },
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "document", "items": ["Maximize", "-", "Source"]},
        ],
    },
)


JSON_CONFIG = json.dumps(WAGTAIL_CKEDITOR_CONFIG)
