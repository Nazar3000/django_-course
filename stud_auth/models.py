from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class StudentProfile(models.Model):
    '''To keep extra user data'''
    # user mapping
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='student_profile')


    class Meta(object):
        verbose_name = _("User Profile")

        # extra user data
    mobile_phone = models.CharField(
        max_length=12,
        blank=True,
        verbose_name=_("Mobile Phone"),
        default='')
    #
    actual_address = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Actual address"),
        default='')
    #
    passportID = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Passport ID"),
        default='')

    photo = models.ImageField(
        blank=True,
        verbose_name=_("Photo"),
        null=True
    )

    def __str__(self):
        return self.user.username
