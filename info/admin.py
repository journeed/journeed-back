from django.contrib import admin
from .models import *

admin.site.register(HomeInfo)
admin.site.register(AboutInfo)
admin.site.register(DifferentInfo)
admin.site.register(ContactInfo)
admin.site.register(Contact)
admin.site.register(PartnershipFeatureInfo)
admin.site.register(PartnershipTypeInfo)
admin.site.register(PartnershipCommissionInfo)
admin.site.register(PartnershipFaqInfo)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "url", )

admin.site.register(SocialMedia, SocialMediaAdmin)

