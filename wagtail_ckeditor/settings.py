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

WAGTAIL_CKEDITOR_FONT_SIZES = "8/8px;9/9px;10/10px;11/11px;12/12px;14/14px;\
    16/16px;18/18px;20/20px;22/22px;24/24px;\
    26/26px;28/28px;36/36px;48/48px;72/72px;"
WAGTAIL_CKEDITOR_FONT_SIZES += getattr(
    settings, "WAGTAIL_CKEDITOR_FONT_SIZES", ""
)

WAGTAIL_CKEDITOR_LINE_HEIGHT = "1px; 2px; 3px; 5px; 10px; 15px;"
WAGTAIL_CKEDITOR_LINE_HEIGHT += getattr(
    settings, "WAGTAIL_CKEDITOR_LINE_HEIGHT", ""
)

WAGTAIL_CKEDITOR_SKIN = getattr(
    settings, "WAGTAIL_CKEDITOR_SKIN", "moono-lisa"
)

WAGTAIL_CKEDITOR_FONT_WEIGHT = (
    "bold;bolder;lighter;normal;100;200;300;400;500;600;700;800;900;"
)

WAGTAIL_CKEDITOR_FONT_WEIGHT += getattr(
    settings, "WAGTAIL_CKEDITOR_FONT_WEIGHT", ""
)
WAGTAIL_CKEDITOR_ALLOWED_CONTENT = getattr(
    settings, "WAGTAIL_CKEDITOR_ALLOWED_CONTENT", "false"
)

WAGTAIL_CKEDITOR_CONFIG = getattr(
    settings,
    "WAGTAIL_CKEDITOR_CONFIG",
    {
        "language": "en",
        "skin": WAGTAIL_CKEDITOR_SKIN,
        "uiColor": "#AADC6E",
        "font_names": WAGTAIL_CKEDITOR_FONTS,
        "fontSize_sizes": WAGTAIL_CKEDITOR_FONT_SIZES,
        "extraPlugins": "lineheight,richcombo,fontweight",
        "mathJaxLib": "//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML",
        "line_height": WAGTAIL_CKEDITOR_LINE_HEIGHT,
        "font_weight": WAGTAIL_CKEDITOR_FONT_WEIGHT,
        "allowedContent": WAGTAIL_CKEDITOR_ALLOWED_CONTENT,
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
                "items": [
                    "Styles",
                    "Format",
                    "Font",
                    "FontSize",
                    "lineheight",
                    "fontweight",
                ],
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

