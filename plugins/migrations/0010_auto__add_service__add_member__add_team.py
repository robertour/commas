# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'cmsplugin_service', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Name', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='Description')),
        ))
        db.send_create_signal(u'plugins', ['Service'])

        # Adding model 'Member'
        db.create_table(u'cmsplugin_member', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Name', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='Description')),
        ))
        db.send_create_signal(u'plugins', ['Member'])

        # Adding model 'Team'
        db.create_table(u'cmsplugin_team', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Name', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='Description')),
        ))
        db.send_create_signal(u'plugins', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'cmsplugin_service')

        # Deleting model 'Member'
        db.delete_table(u'cmsplugin_member')

        # Deleting model 'Team'
        db.delete_table(u'cmsplugin_team')


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
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
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
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
        },
        u'plugins.team': {
            'Meta': {'object_name': 'Team', 'db_table': "u'cmsplugin_team'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Description'"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Name'", 'max_length': '100'})
        }
    }

    complete_apps = ['plugins']