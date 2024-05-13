import pathlib


def validate_photo(photo):
    if photo:
        photo_path = pathlib.Path(str(photo)).suffix
        # validate photo format
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.heic']

        return photo_path in allowed_extensions
    pass
