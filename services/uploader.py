from django.template.defaultfilters import slugify


class Uploader:
    @staticmethod
    def user_profile_uploader(instance, filename):
        return f"profile/{instance.user.email}/{filename}"

    @staticmethod
    def head_background_uploader(instance, filename):
        return f"home/{instance}/{filename}"

    @staticmethod
    def special_offer_image_uploader(instance, filename):
        return f"special-offer/{instance.user.full_name}/{filename}"

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
    def blog_image_uploader(instance, filename):
        return f"blog/{instance.user.full_name}/{filename}"

    @staticmethod
    def advice_image_uploader(instance, filename):
        return f"advice/{instance.user.full_name}/{filename}"

    @staticmethod
    def gallery_image_uploader(instance, filename):
        return f"gallery/{filename}"

    @staticmethod
    def pastime_photo_uploader(instance, filename):
        return f"pastime-type/{filename}"

    @staticmethod
    def partnership_photo_uploader(instance, filename):
        return f"partnership/{instance.user}/{filename}"

    @staticmethod
    def partnership_type_photo_uploader(instance, filename):
        return f"partnership-type/{instance.title}/{filename}"
