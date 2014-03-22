from cms.models import Page
from django.db.models.signals import post_save
from cms.models.pluginmodel import CMSPlugin

def signal_handler(instance, **kwargs):
    if not isinstance(instance, CMSPlugin):
       return
    page = Page.objects.get(reverse_id='general', publisher_is_draft = True)
    if page.placeholders.filter(pk=instance.placeholder_id).exists():
        page.publish()

post_save.connect(signal_handler)
