from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from services.mixin import DateMixin

User = get_user_model()


class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


class Partnership(DateMixin):
    role = models.OneToOneField(Role, on_delete=models.SET_NULL, null=True, blank=True)
    partner_photo = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    mobile = PhoneNumberField(null=True, unique=True)

    def __str__(self):
        return f'{self.name} - {self.role}'

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Partnership'
        verbose_name_plural = 'Partnerships'

