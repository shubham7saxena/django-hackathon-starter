from __future__ import unicode_literals

import datetime
import random
import re

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, transaction
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now as datetime_now
from django.utils import six

from .users import UserModel, UserModelString

class RegistrationManager(models.Manager):

    def create_inactive_user(self, site, new_user=None,
                             request=None, profile_info={}, **user_info):
        if new_user is None:
            password = user_info.pop('password')
            new_user = UserModel()(**user_info)
            new_user.set_password(password)
        new_user.is_active = True

        new_user.date_joined = datetime_now()

        with transaction.atomic():
            new_user.save()
            registration_profile = self.create_profile(
                new_user, **profile_info)

        return new_user

    def create_profile(self, user, **profile_info):
        profile = self.model(user=user, **profile_info)

        profile.save()

        return profile

@python_2_unicode_compatible
class RegistrationProfile(models.Model):

    user = models.OneToOneField(
        UserModelString(),
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )

    objects = RegistrationManager()

    class Meta:
        verbose_name = _('registration profile')
        verbose_name_plural = _('registration profiles')

    def __str__(self):
        return str(self.user)
