from django import forms
from cmsplugin_contact.forms import ContactForm

class CustomContactForm(ContactForm):
    name = forms.CharField()
    phone = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CustomContactForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['name', 'phone', 'email', 'subject', 'content']
