# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Service.cropping'
        db.delete_column(u'cmsplugin_service', 'cropping')


    def backwards(self, orm):
        # Adding field 'Service.cropping'
        db.add_column(u'cmsplugin_service', 'cropping',
                      self.gf(u'django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'plugins.credential': {
            'Meta': {'object_name': 'Credential', 'db_table': "u'cmsplugin_credential'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'inverted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
        },
        u'plugins.member': {
            'Meta': {'object_name': 'Member', 'db_table': "u'cmsplugin_member'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/person-placeholder.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Job Title'", 'max_length': '100'}),
            'twitter': ('django.db.models.fields.URLField', [], {'default': "'http://twitter.com'", 'max_length': '200'})
        },
        u'plugins.reference': {
            'Meta': {'object_name': 'Reference', 'db_table': "u'cmsplugin_reference'", '_ormbases': ['cms.CMSPlugin']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'referee': ('django.db.models.fields.CharField', [], {'default': "'Referee'", 'max_length': '100'})
        },
        u'plugins.service': {
            'Meta': {'object_name': 'Service', 'db_table': "u'cmsplugin_service'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
        },
        u'plugins.team': {
            'Meta': {'object_name': 'Team', 'db_table': "u'cmsplugin_team'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
        },
        u'plugins.widget': {
            'Meta': {'object_name': 'Widget', 'db_table': "u'cmsplugin_widget'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['plugins']