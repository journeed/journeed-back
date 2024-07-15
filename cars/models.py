from django.db import models
from services.choices import RATING
from services.slugify import unique_slug_generator
from services.mixin import DateMixin, SlugMixin
from services.uploader import Uploader
from django.contrib.auth import get_user_model

User = get_user_model()


class NameAbstract(DateMixin):
    name = models.CharField(max_length=70)

    class Meta:
        abstract = True


class CarCategory(NameAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "Car categories"


class Steering(NameAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "steering"
        verbose_name_plural = "Steering"


class Fuel(NameAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "fuel"
        verbose_name_plural = "Car fuels"


class Car(NameAbstract, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"is_partnership": True})
    type_car = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    description = models.TextField()
    steering = models.ForeignKey(Steering, on_delete=models.CASCADE)
    person_count = models.PositiveIntegerField(default=2)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)
    fuel_volume = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "Cars"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, slug_name=self.name)
        super().save(*args, **kwargs)


class CarImage(DateMixin):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.car_image_uploader)

    def __str__(self):
        return self.car.name

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "Car images"


class CarReview(DateMixin):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=RATING)

    def __str__(self):
        return self.user.email

    class Meta:
        unique_together = ('car', 'user')
        ordering = ("-created_at", )
        verbose_name = "review"
        verbose_name_plural = "Car reviews"


class CarWishlist(DateMixin):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.name

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "Car wishlist"



