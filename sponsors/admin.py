from django.contrib import admin
from organizations.models import Organization, OrganizationUser, OrganizationOwner
from .forms import SponsorUserForm
from .models import Sponsor, SponsorUser
"""
from .forms import SponsorForm
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    form = SponsorForm

admin.site.register(Sponsor, SponsorAdmin)
""" 

class SponsorUserAdmin(admin.ModelAdmin):
    model = SponsorUser
    form = SponsorUserForm
    readonly_fields = ('user',)

admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)
admin.site.register(Sponsor)
admin.site.register(SponsorUser, SponsorUserAdmin)



"""
class DonorInline(admin.StackedInline):
    model = Donor
    can_delete = False
    verbose_name_plural = 'Donor Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None,              {'fields': ['username']}),
        ('Personal Info',   {'fields': ['first_name', 'last_name', 'email', 'password'], 'classes': ['collapse']}),
        ('Permissions',     {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'], 'classes': ['collapse']}),
        ('Important Dates', {'fields': ['date_joined', 'last_login'], 'classes': ['collapse']}),
    ]

    inlines = [DonorInline, ]
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
"""
