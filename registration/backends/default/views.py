from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

from ... import signals
from ...models import RegistrationProfile
from ...views import RegistrationView as BaseRegistrationView
from ...users import UserModel


class RegistrationView(BaseRegistrationView):

    success_url = 'registration_complete'

    def register(self, form):
        
        site = get_current_site(self.request)

        if hasattr(form, 'save'):
            new_user_instance = form.save()
        else:
            new_user_instance = (UserModel().objects
                                 .create_user(**form.cleaned_data))

        new_user = RegistrationProfile.objects.create_inactive_user(
            new_user=new_user_instance,
            site=site,
            request=self.request,
        )
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user
