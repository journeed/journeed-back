from django.contrib import admin
from .models import HomeInfo, AboutInfo, DifferentInfo, SocialMedia, ContactInfo

admin.site.register(HomeInfo)
admin.site.register(AboutInfo)
admin.site.register(DifferentInfo)
admin.site.register(ContactInfo)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "url", )

admin.site.register(SocialMedia, SocialMediaAdmin)

