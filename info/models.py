from django.db import models
from services.mixin import DateMixin
from phonenumber_field.modelfields import PhoneNumberField
from services.uploader import Uploader


class HomeInfo(DateMixin):
    head = models.CharField(max_length=200)
    first_content = models.TextField(null=True, blank=True)
    second_content = models.TextField(null=True, blank=True)
    home_background = models.ImageField(upload_to=Uploader.head_background_uploader)
    home_banner = models.TextField()
    home_banner_background = models.ImageField(upload_to=Uploader.head_background_uploader)

    def __str__(self):
        return "Home Info"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # preventing the creation of a second object
        self.__class__.objects.exclude(id=self.id).delete()


class AboutInfo(DateMixin):
    slogan = models.CharField(max_length=300)
    head = models.CharField(max_length=300)
    background = models.ImageField(upload_to=Uploader.about_background_uploader, null=True)
    first_content = models.TextField()
    second_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'About Text'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()


class DifferentInfo(DateMixin):
    head = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return 'About Different'


class SocialMedia(DateMixin):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class ContactInfo(DateMixin):
    mobile = PhoneNumberField()
    mail = models.EmailField()
    work_time = models.CharField(max_length=400)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.SET_NULL, null=True, blank=True)
    map = models.URLField()

    def __str__(self):
        return 'Contact Info'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()


class Contact(DateMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    request_type = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
