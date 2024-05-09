from django.template.defaultfilters import slugify


class Uploader:
    @staticmethod
    def user_profile_uploader(instance, filename):
        return f"profile/{instance.user.email}/{filename}"

    @staticmethod
    def head_background_uploader(instance, filename):
        return f"home/{instance}/{filename}"

    @staticmethod
    def car_image_uploader(instance, filename):
        return f"cars/{slugify(instance.car.name)}/{filename}"
