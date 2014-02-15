from cms.models.pluginmodel import CMSPlugin
from django_jcrop.models import JCropImageField

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


class Widget(CMSPlugin):
    heading = models.CharField(max_length=100, verbose_name='Title',
        null=True, blank=True)
    body = models.TextField(verbose_name='Body')
