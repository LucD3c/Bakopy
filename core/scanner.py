import os

FILE_CATEGORIES = {
    "Documentos": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".txt", ".odt", ".ods", ".odp", ".rtf", ".csv", ".md",
    ],
    "Imagenes": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
        ".webp", ".svg", ".ico", ".raw", ".heic", ".heif",
    ],
    "Videos": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm",
        ".m4v", ".3gp", ".mpeg", ".mpg",
    ],
    "Musica": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a",
        ".opus", ".aiff",
    ],
    "Comprimidos": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
    ],
    "Codigo": [
        ".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp",
        ".cs", ".php", ".rb", ".go", ".rs", ".sh", ".bat", ".ps1",
        ".json", ".xml", ".yaml", ".yml", ".sql",
    ],
}


def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Otros"
