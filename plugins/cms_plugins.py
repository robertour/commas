from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import Credential, Reference, Service, Team, Member


class CredentialPlugin(CMSPluginBase):
    model = Credential
    name = _("Crendential Plugin")
    render_template = "credential.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CredentialPlugin)


class ReferencePlugin(CMSPluginBase):
    model = Reference
    name = _("Reference Plugin")
    render_template = "reference.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ReferencePlugin)


class ServicePlugin(CMSPluginBase):
    model = Service
    name = _("Service Plugin")
    render_template = "service.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ServicePlugin)


class TeamPlugin(CMSPluginBase):
    model = Team
    name = _("Team Plugin")
    render_template = "team.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TeamPlugin)


class MemberPlugin(CMSPluginBase):
    model = Member
    name = _("Member Plugin")
    render_template = "member.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(MemberPlugin)