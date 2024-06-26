from django.contrib import admin
from .models import Car, CarImage, CarCategory, CarReview, Steering, CarWishlist, Fuel


admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarCategory)
admin.site.register(CarReview)
admin.site.register(Steering)
admin.site.register(CarWishlist)
admin.site.register(Fuel)
