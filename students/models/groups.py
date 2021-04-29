# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    '''Group Model'''

    class Meta(object):
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Title"))

    leader = models.OneToOneField('Student',
                                  verbose_name=_("Leader"),
                                  blank=True,
                                  null=True,
                                  on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=_("Extra Notes"))

    # Отображает имя группы в админке

    # variant for old django version 1.7
    # def __unicode__(self):
    #     if self.leader:
    #         return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
    #     else:
    #         return u"%s" % (self.title,)

    # new variant
    def __str__(self):
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name,
                                   self.leader.last_name)
        else:
            return "%s" % (self.title,)