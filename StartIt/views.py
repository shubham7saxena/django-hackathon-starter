from django.views import generic
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
import requests

from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash

class HomePage(generic.TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        user = get_user(self,User)
        context = super(HomePage, self).get_context_data(**kwargs)
        context["user"] = user
        return context

def get_user(self,User):
    return User.objects.get(id = self.request.session['_auth_user_id'])
