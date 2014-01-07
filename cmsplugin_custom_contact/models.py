from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _

class CustomContact(BaseContact):
    name_label = models.CharField(
      verbose_name=_('Name sender label'), 
      default=_('Name'), max_length=20)
    phone_label = models.CharField(
      verbose_name=_('Phone sender label'), 
      default=_('Phone'), max_length=20)
