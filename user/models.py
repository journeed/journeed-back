from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager
from services.generator import CodeGenerator
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from services.mixin import DateMixin
from services.uploader import Uploader


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120)
    full_name = models.CharField(max_length=250)

    mobile = PhoneNumberField(null=True, unique=True)
    country = CountryField()

    slug = models.SlugField(unique=True)
    activation_code = models.CharField(max_length=6, blank=True, null=True, editable=False)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_partnership = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name",]

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "User"
        verbose_name_plural = "User Accounts"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = CodeGenerator.create_slug_shortcode(size=20, model_=self.__class__)
        return super(User, self).save(*args, **kwargs)


class Profile(DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=Uploader.user_profile_uploader, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "User profiles"





