from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from services.mixin import DateMixin
from services.uploader import Uploader

User = get_user_model()


class Partnership(DateMixin):
    partner_photo = models.ImageField(upload_to=Uploader.partnership_photo_uploader)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True)
    about = models.TextField()
    mobile = PhoneNumberField(null=True, unique=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Partnership'
        verbose_name_plural = 'Partnerships'


class RentCar(DateMixin):
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.partnership.user


class Hotels(DateMixin):
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.partnership.user


class Restaurant(DateMixin):
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.partnership.user


class Guide(DateMixin):
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.partnership.user


class Flight(DateMixin):
    partnership = models.ForeignKey(Partnership, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.partnership.user


class PartnershipApplication(DateMixin):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    partnership_method = models.CharField(max_length=100)
    currency = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Partnership Application'
        verbose_name_plural = 'Partnership Applications'



