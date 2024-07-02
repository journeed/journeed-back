import pathlib

photo_ext = ['.jpg', '.jpeg', '.png', '.heic']
video_photo_ext = ['.mkv', '.mp4', '.mov', '.jpg', '.jpeg', '.png', '.gif', '.heic']


def validate_photo(photo):
    if photo:
        photo_path = pathlib.Path(str(photo)).suffix

        return photo_path in photo_ext
    pass


def validate_photo_and_video(photo):
    if photo:
        file_path = pathlib.Path(str(photo)).suffix

        return file_path in video_photo_ext
    pass



