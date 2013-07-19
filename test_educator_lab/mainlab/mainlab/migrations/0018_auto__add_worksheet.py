# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Worksheet'
        db.create_table(u'mainlab_worksheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['mainlab.MyUser'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')()),
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('timeModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('userModified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['mainlab.MyUser'])),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Worksheet'])

        # Adding M2M table for field chapters on 'Worksheet'
        db.create_table(u'mainlab_worksheet_chapters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worksheet', models.ForeignKey(orm[u'mainlab.worksheet'], null=False)),
            ('chapter', models.ForeignKey(orm[u'mainlab.chapter'], null=False))
        ))
        db.create_unique(u'mainlab_worksheet_chapters', ['worksheet_id', 'chapter_id'])

        # Adding M2M table for field files on 'Worksheet'
        db.create_table(u'mainlab_worksheet_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worksheet', models.ForeignKey(orm[u'mainlab.worksheet'], null=False)),
            ('file', models.ForeignKey(orm[u'mainlab.file'], null=False))
        ))
        db.create_unique(u'mainlab_worksheet_files', ['worksheet_id', 'file_id'])


    def backwards(self, orm):
        # Deleting model 'Worksheet'
        db.delete_table(u'mainlab_worksheet')

        # Removing M2M table for field chapters on 'Worksheet'
        db.delete_table('mainlab_worksheet_chapters')

        # Removing M2M table for field files on 'Worksheet'
        db.delete_table('mainlab_worksheet_files')


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