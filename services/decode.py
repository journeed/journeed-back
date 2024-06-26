import base64
from django.core.files.base import ContentFile


def decodebase64_image(image):
    format, imgstr = image.split(';base64,')
    ext = format.split('/')[-1]

    if ext not in ['jpg', 'jpeg', 'png', 'heic']:
        return None

    # Decode the base64 string
    img_data = base64.b64decode(imgstr)

    # Create a file
    image_name = f"uploaded_image.{ext}"

    image_file = ContentFile(img_data, name=image_name)

    return image_file
