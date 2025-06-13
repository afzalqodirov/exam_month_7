from django.db import models
from api_papers.models import categories

# experiment!
from django_prose_editor.fields import ProseEditorField

class JournalsModel_UZ(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = ProseEditorField(extensions={
            # Core text formatting
            "Bold": True,
            "Italic": True,
            "Strike": True,
            "Underline": True,
            "HardBreak": True,

            # Structure
            "Heading": {
                "levels": [1, 2, 3]  # Only allow h1, h2, h3
            },
            "BulletList": True,
            "OrderedList": True,
            "Blockquote": True,

            # Advanced extensions
            "Link": {
                "enableTarget": True,  # Enable "open in new window"
                "protocols": ["http", "https", "mailto"],  # Limit protocols
            },
            "Table": True,

            # Editor capabilities
            "History": True,       # Enables undo/redo
            "HTML": True,          # Allows HTML view
            "Typographic": True,   # Enables typographic chars
        },
            sanitize=True)
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

class JournalsModel_RU(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = ProseEditorField(extensions={
            # Core text formatting
            "Bold": True,
            "Italic": True,
            "Strike": True,
            "Underline": True,
            "HardBreak": True,

            # Structure
            "Heading": {
                "levels": [1, 2, 3]  # Only allow h1, h2, h3
            },
            "BulletList": True,
            "OrderedList": True,
            "Blockquote": True,

            # Advanced extensions
            "Link": {
                "enableTarget": True,  # Enable "open in new window"
                "protocols": ["http", "https", "mailto"],  # Limit protocols
            },
            "Table": True,

            # Editor capabilities
            "History": True,       # Enables undo/redo
            "HTML": True,          # Allows HTML view
            "Typographic": True,   # Enables typographic chars
        },
            sanitize=True)
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()

class JournalsModel_EN(models.Model):
    image = models.ImageField(upload_to='journals/', default="'profile pictures'/pic.png")
    title = models.CharField(max_length=200)
    article = ProseEditorField(extensions={
            # Core text formatting
            "Bold": True,
            "Italic": True,
            "Strike": True,
            "Underline": True,
            "HardBreak": True,

            # Structure
            "Heading": {
                "levels": [1, 2, 3]  # Only allow h1, h2, h3
            },
            "BulletList": True,
            "OrderedList": True,
            "Blockquote": True,

            # Advanced extensions
            "Link": {
                "enableTarget": True,  # Enable "open in new window"
                "protocols": ["http", "https", "mailto"],  # Limit protocols
            },
            "Table": True,

            # Editor capabilities
            "History": True,       # Enables undo/redo
            "HTML": True,          # Allows HTML view
            "Typographic": True,   # Enables typographic chars
        },
            sanitize=True)
    reference = models.CharField(max_length=30, choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField()
