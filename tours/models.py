from django.db import models
from services.mixin import DateMixin, SlugMixin
from basemodels.models import City
from django.contrib.auth import get_user_model
from services.choices import RATING
from services.slugify import unique_slug_generator
from services.uploader import Uploader
from partnership.models import TourOrganizer

User = get_user_model()


class Tour(DateMixin, SlugMixin):
    user = models.ForeignKey(TourOrganizer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=Uploader.special_offer_tour_uploader)
    day_duration = models.CharField(max_length=150)
    child_count = models.PositiveIntegerField()
    young_count = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'Tour: {self.city.country.name} - {self.city.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, slug_name=f'{self.city.country.name}-{self.city.name}')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = "Tour"
        verbose_name_plural = "Tours"


class TourReview(DateMixin):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=None)
    content = models.TextField()

    def __str__(self):
        return self.user.full_name

    class Meta:
        unique_together = ('tour', 'user')
        ordering = ("-created_at", )
        verbose_name = "Tour Review"
        verbose_name_plural = "Tour Reviews"
