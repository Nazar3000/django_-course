from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class StProfile(models.Model):
    '''To keep extra user data'''
    # user mapping
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='student_profile')


    class Meta(object):
        verbose_name = _(u"User Profile")

        # extra user data
    mobile_phone = models.CharField(
        max_length=12,
        blank=True,
        verbose_name=_(u"Mobile Phone"),
        default='')
    #
    actual_address = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_(u"Actual address"),
        default='')
    #
    passportID = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_(u"Passport ID"),
        default='')

    photo = models.ImageField(
        blank=True,
        verbose_name=_(u"Photo"),
        null=True
    )

    def __unicode__(self):
        return self.user.username
