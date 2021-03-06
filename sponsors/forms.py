from django import forms
from django.conf import settings
from django.contrib.sites.models import Site
from organizations.backends import invitation_backend
from sponsors.models import Sponsor, SponsorUser
"""
class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('name', 'ein', 'website', 'zipcode',)
"""

class SponsorUserForm(forms.ModelForm):
    """
    Form class for editing OrganizationUsers *and* the linked user model.
    """
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()

    class Meta:
        model = SponsorUser
        exclude = ('is_admin',)
        

    def __init__(self, *args, **kwargs):
        super(SponsorUserForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, *args, **kwargs):
        """
        This method saves changes to the linked user model.
        """
        if self.instance.pk is None:
            site = Site.objects.get(pk=settings.SITE_ID)
            self.instance.user = invitation_backend().invite_by_email(
                    self.cleaned_data['email'],
                    **{'first_name': self.cleaned_data['first_name'],
                        'last_name': self.cleaned_data['last_name'],
                        'organization': self.cleaned_data['organization'],
                        'domain': site})
        # self.instance.user.first_name = self.cleaned_data['first_name']
        # self.instance.user.last_name = self.cleaned_data['last_name']
        # self.instance.user.email = self.cleaned_data['email']
        # self.instance.user.save()
        return super(SponsorUserForm, self).save(*args, **kwargs)