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

    @staticmethod
    def about_background_uploader(instance, filename):
        return f"about/{instance}/{filename}"

    @staticmethod
    def story_uploader(instance, filename):
        return f"story/{instance.user.full_name}/{filename}"

    @staticmethod
    def partnership_photo_uploader(instance, filename):
        return f"partnership/{instance.user}/{filename}"

    @staticmethod
    def partnership_type_photo_uploader(instance, filename):
        return f"partnership-type/{instance.title}/{filename}"
