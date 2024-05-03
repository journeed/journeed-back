class Uploader:

    @staticmethod
    def user_profile_uploader(instance, filename):
        return f"profile/{instance.user.email}/{filename}"

    @staticmethod
    def head_background_uploader(instance, filename):
        return f"home/{instance}/{filename}"
