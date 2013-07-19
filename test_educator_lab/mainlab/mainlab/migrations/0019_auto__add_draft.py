# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Draft'
        db.create_table(u'mainlab_draft', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainlab.MyUser'], unique=True, primary_key=True)),
            ('resourceType', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('goals', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('materials', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('lesson', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Draft'])


    def backwards(self, orm):
        # Deleting model 'Draft'
        db.delete_table(u'mainlab_draft')


    models = {
        u'mainlab.activity': {
            'Meta': {'object_name': 'Activity'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'goals': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('tinymce.models.HTMLField', [], {}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"}),
            'materials': ('tinymce.models.HTMLField', [], {}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'userModified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"})
        },
        u'mainlab.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'hasResource': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Subject']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.comment': {
            'Meta': {'object_name': 'Comment'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Activity']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Project']", 'null': 'True', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']"})
        },
        u'mainlab.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'hasResource': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.draft': {
            'Meta': {'object_name': 'Draft'},
            'goals': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'lesson': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'materials': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'resourceType': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mainlab.MyUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainlab.file': {
            'Meta': {'object_name': 'File'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'doc': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mainlab.grade': {
            'Curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Curriculum']"}),
            'Meta': {'object_name': 'Grade'},
            'hasResource': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        'mainlab.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'mainlab.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'goals': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('tinymce.models.HTMLField', [], {}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"}),
            'materials': ('tinymce.models.HTMLField', [], {}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'userModified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"})
        },
        u'mainlab.subject': {
            'Meta': {'object_name': 'Subject'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Grade']"}),
            'hasResource': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.worksheet': {
            'Meta': {'object_name': 'Worksheet'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'description': ('tinymce.models.HTMLField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'userModified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['mainlab.MyUser']"})
        }
    }

    complete_apps = ['mainlab']