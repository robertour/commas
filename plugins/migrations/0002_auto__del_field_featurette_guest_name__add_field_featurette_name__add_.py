# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Featurette.guest_name'
        db.delete_column(u'cmsplugin_featurette', 'guest_name')

        # Adding field 'Featurette.name'
        db.add_column(u'cmsplugin_featurette', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Name', max_length=100),
                      keep_default=False)

        # Adding field 'Featurette.text'
        db.add_column(u'cmsplugin_featurette', 'text',
                      self.gf('django.db.models.fields.TextField')(default='Description'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Featurette.guest_name'
        db.add_column(u'cmsplugin_featurette', 'guest_name',
                      self.gf('django.db.models.fields.CharField')(default='Guest', max_length=50),
                      keep_default=False)

        # Deleting field 'Featurette.name'
        db.delete_column(u'cmsplugin_featurette', 'name')

        # Deleting field 'Featurette.text'
        db.delete_column(u'cmsplugin_featurette', 'text')


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
        u'plugins.featurette': {
            'Meta': {'object_name': 'Featurette', 'db_table': "u'cmsplugin_featurette'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Description'"})
        }
    }

    complete_apps = ['plugins']