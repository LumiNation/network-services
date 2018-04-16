from django.core.validators import MinLengthValidator
from django.db import models
from organizations.models import Organization, OrganizationUser

# from sector_meta.utils import phone_regex


class Sponsor(Organization):
    ein 	= models.CharField(
    	primary_key=True, 
    	unique=True, 
    	max_length=9, 
    	validators=[MinLengthValidator(4),]
    	)
    # phone 	= models.CharField(validators=[phone_regex,], max_length=17, blank=True)
    website = models.URLField(blank=True, max_length=20)
    zipcode = models.CharField(blank=True, max_length=5)


class SponsorUser(OrganizationUser):
    class Meta:
        proxy = True

"""
Sponsor
	-Details-
	Socia Media Links
	Causes
	
	-Components-
	Projects
	Roles
	SponsorUsers
	

SponsorUser
	

Roles
	Permissions

Permissions
	Project Creation


Default Roles
	Executive Director
	

"""