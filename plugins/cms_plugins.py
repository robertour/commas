from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugins.text.models import Text
from cms.plugins.text.cms_plugins import TextPlugin as TextPluginCMS
from cmsplugin_filer_file.cms_plugins import FilerFilePlugin
from django.contrib.admin import TabularInline

from models import Credential, Reference, Service, Team, Member, Widget, SocialLink


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

class SocialLinkInline(TabularInline):
    model = SocialLink
    extra = 1

class MemberPlugin(CMSPluginBase):
    model = Member
    name = _("Member Plugin")
    render_template = "member.html"
    module = 'Commas & Industry'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    inlines = [SocialLinkInline]

plugin_pool.register_plugin(MemberPlugin)


class TextPlugin(CMSPluginBase):
    model = Text
    name = _("Text/HTML Plugin")
    render_template = "text.html"

plugin_pool.unregister_plugin(TextPluginCMS)
plugin_pool.register_plugin(TextPlugin)


class EditorTextPlugin(TextPluginCMS):
    name = _("TinyMCE Text Plugin")

plugin_pool.register_plugin(EditorTextPlugin)

class FilerBackgroundImage(FilerFilePlugin):
    name = _("Background Image")
    exclude = ['title', 'target_blank']
    render_template = "background_image.html"

plugin_pool.register_plugin(FilerBackgroundImage)

class WidgetPlugin(CMSPluginBase):
    model = Widget
    name = _("Sidebar Widget Plugin")
    render_template = "widget.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(WidgetPlugin)
