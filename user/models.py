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


def upload_to(instance, filename):
    return f"users/{instance.email}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120)
    full_name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    mobile = PhoneNumberField(null=True, unique=True)
    country = CountryField()

    slug = models.SlugField(unique=True)
    activation_code = models.CharField(max_length=6, blank=True, null=True, editable=False)

    timestamp = models.DateTimeField(auto_now_add=True)
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




