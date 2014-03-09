from cms.models.pluginmodel import CMSPlugin
from django_jcrop.models import JCropImageField
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Credential(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    image = models.ImageField(upload_to='featurettes')
    inverted = models.BooleanField(
        verbose_name='Image on the right?',
        help_text='Check if you want the image on the right',
        default=False)


class Reference(CMSPlugin):
    referee = models.CharField(max_length=100, default='Referee')
    description = models.TextField(default='Description')
    active = models.BooleanField(
        verbose_name='Is the active reference?',
        help_text='Check to make it appear first',
        default=False)


class Service(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    image = models.ImageField(blank=True, null=True, upload_to='services')

class Team(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')


class Member(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    title = models.CharField(max_length=100, default='Job Title')
    description = models.TextField(default='Description',
        verbose_name="Bios")
    twitter = models.URLField(max_length=200, default='http://twitter.com',
        verbose_name="Twitter URL")
    image = JCropImageField(upload_to='members', blank=True)

    def copy_relations(self, oldinstance):
        for associated_link in oldinstance.associated_link.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_link.pk = None
            associated_link.plugin = self
            associated_link.save()

class SocialLink(models.Model):
    plugin = models.ForeignKey( Member, related_name="associated_link" )
    social_network = models.CharField(max_length=100, default='', 
      null=True, blank=True, verbose_name=_("Social Nework Name"))
    url = models.URLField(_("Social Network URL"), null=False, blank=False, 
      default=None)
    icon = FilerImageField(null=True, blank=True, default=None, 
      verbose_name=_("Icon"))


class Widget(CMSPlugin):
    heading = models.CharField(max_length=100, verbose_name='Title',
        null=True, blank=True)
    body = models.TextField(verbose_name='Body')
