from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from profiles.models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None,              {'fields': ['username']}),
        ('Personal Info',   {'fields': ['first_name', 'last_name', 'email', 'password'], 'classes': ['collapse']}),
        ('Permissions',     {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'], 'classes': ['collapse']}),
        ('Important Dates', {'fields': ['date_joined', 'last_login'], 'classes': ['collapse']}),
    ]

    inlines = [ProfileInline, ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'date_joined', 'is_active']
    # list_filter = []
    # search_fields = []

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
