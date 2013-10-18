from cms.models.pluginmodel import CMSPlugin

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


class Team(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')


class Member(CMSPlugin):
    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
