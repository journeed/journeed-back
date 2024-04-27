from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):

    list_display = (
        "email",
        "full_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_active", "is_superuser")
    fieldsets = (
        (
            "User information",
            {
                "fields": (
                    "email",
                    "full_name",
                    "country",
                    "mobile",
                    "password",
                    "logo",
                )
            },
        ),
        ("Permissions", {"fields": ("groups", "user_permissions", "is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            "Create new user",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "full_name",
                    "country",
                    "mobile",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    readonly_fields = ("timestamp",)
    search_fields = ("email", "full_name")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

