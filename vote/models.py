from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from votelist import us_states, us_parties


class UserInfo(models.Model):
    # person fields
    user = models.OneToOneField(User)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    phone_regex = RegexValidator(regex='^\+?1?\d{9, 15}$',
                                 message="Phone number must be in the format: '+9999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=15, blank=True)

    # location fields
    street_home = models.TextField(blank=True)
    city_home = models.CharField(max_length=128, blank=True)
    state_home = models.CharField(max_length=2, choices=us_states, blank=True)
    zip_home = models.CharField(max_length=10, blank=True)

    # voting fields
    party = models.CharField(max_length=10, choices=us_parties, blank=True)

    # override instance return
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username