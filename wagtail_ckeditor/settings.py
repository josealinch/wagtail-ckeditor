import json

from django.conf import settings

WAGTAIL_CKEDITOR_FONTS = """
    Arial/Arial, Helvetica, sans-serif;\
    Comic Sans MS/Comic Sans MS, cursive;\
    Courier New/Courier New, Courier, monospace;\
    Georgia/Georgia, serif;\
    Lucida Sans Unicode/Lucida Sans Unicode, Lucida Grande, sans-serif;\
    Tahoma/Tahoma, Geneva, sans-serif;\
    Times New Roman/Times New Roman, Times, serif;\
    Trebuchet MS/Trebuchet MS, Helvetica, sans-serif;\
    Verdana/Verdana, Geneva, sans-serif;\
"""

WAGTAIL_CKEDITOR_FONTS += getattr(settings, "WAGTAIL_CKEDITOR_FONTS", "")

WAGTAIL_CKEDITOR_CONFIG = getattr(
    settings,
    "WAGTAIL_CKEDITOR_CONFIG",
    {
        "language": "en",
        "skin": "moono-dark",
        "font_names": WAGTAIL_CKEDITOR_FONTS,
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
            {
                "name": "styles",
                "items": ["Styles", "Format", "Font", "FontSize"],
            },
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
