from django.db import models
from django.db.models.signals import post_save
from users.models import CustomUser as User
from django.dispatch import receiver

class Donor(models.Model):
    def __str__(self):
        return self.user.username

    # Identification
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    zipcode = models.CharField(blank=True, max_length=5)


    # Giving Statistics
    #donations: list[Donation]
    #donation_tot: big-int          - evaluated
    #social_score: big-int
    #donor_dollars: big-int
    #causes_reported: list[Cause]
    #causes_supported: list[Cause]  - evaluated

    # Project Info
    #proj_following: list[Project]
    #proj_supported: list[Project]  - evaluated
    #proj_fav: list[Project]
    #spon_supported: list[Sponsor]  - evaluated
    #spon_fav: list[Sponsor]


@receiver(post_save, sender=User)
def create_donor_profile(sender, instance, created, **kwargs):
    """
    create profile to match user
    """
    if created:
        Donor.objects.create(user=instance)

"""
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    UserProfile.objects.get(user=User).save()
"""



"""
STUDENT = 1
TEACHER = 2
SUPERVISOR = 3
ROLE_CHOICES = (
    (STUDENT, 'Student'),
    (TEACHER, 'Teacher'),
    (SUPERVISOR, 'Supervisor'),
)
role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
was_published_recently.admin_order_field = 'pub_date'
was_published_recently.short_description = 'Published recently?'
"""
