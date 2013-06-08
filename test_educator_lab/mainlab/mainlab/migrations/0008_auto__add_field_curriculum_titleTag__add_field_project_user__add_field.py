# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Curriculum.titleTag'
        db.add_column(u'mainlab_curriculum', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Project.user'
        db.add_column(u'mainlab_project', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Project.titleTag'
        db.add_column(u'mainlab_project', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Foldable.titleTag'
        db.add_column(u'mainlab_foldable', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Activity.user'
        db.add_column(u'mainlab_activity', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Activity.titleTag'
        db.add_column(u'mainlab_activity', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Grade.titleTag'
        db.add_column(u'mainlab_grade', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Subject.titleTag'
        db.add_column(u'mainlab_subject', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Chapter.titleTag'
        db.add_column(u'mainlab_chapter', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Organizer.user'
        db.add_column(u'mainlab_organizer', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Organizer.titleTag'
        db.add_column(u'mainlab_organizer', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'GraphicOrganizer.titleTag'
        db.add_column(u'mainlab_graphicorganizer', 'titleTag',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Curriculum.titleTag'
        db.delete_column(u'mainlab_curriculum', 'titleTag')

        # Deleting field 'Project.user'
        db.delete_column(u'mainlab_project', 'user_id')

        # Deleting field 'Project.titleTag'
        db.delete_column(u'mainlab_project', 'titleTag')

        # Deleting field 'Foldable.titleTag'
        db.delete_column(u'mainlab_foldable', 'titleTag')

        # Deleting field 'Activity.user'
        db.delete_column(u'mainlab_activity', 'user_id')

        # Deleting field 'Activity.titleTag'
        db.delete_column(u'mainlab_activity', 'titleTag')

        # Deleting field 'Grade.titleTag'
        db.delete_column(u'mainlab_grade', 'titleTag')

        # Deleting field 'Subject.titleTag'
        db.delete_column(u'mainlab_subject', 'titleTag')

        # Deleting field 'Chapter.titleTag'
        db.delete_column(u'mainlab_chapter', 'titleTag')

        # Deleting field 'Organizer.user'
        db.delete_column(u'mainlab_organizer', 'user_id')

        # Deleting field 'Organizer.titleTag'
        db.delete_column(u'mainlab_organizer', 'titleTag')

        # Deleting field 'GraphicOrganizer.titleTag'
        db.delete_column(u'mainlab_graphicorganizer', 'titleTag')


    models = {
        u'mainlab.activity': {
            'Meta': {'object_name': 'Activity'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'foldables': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Foldable']", 'symmetrical': 'False', 'blank': 'True'}),
            'goals': ('tinymce.models.HTMLField', [], {}),
            'graphicOrgs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.GraphicOrganizer']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Item']", 'symmetrical': 'False', 'blank': 'True'}),
            'lesson': ('tinymce.models.HTMLField', [], {}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Link']", 'symmetrical': 'False', 'blank': 'True'}),
            'materials': ('tinymce.models.HTMLField', [], {}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'time': ('tinymce.models.HTMLField', [], {}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'})
        },
        u'mainlab.chapter': {
            'Meta': {'object_name': 'Chapter'},
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
            'organizer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Organizer']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Project']", 'null': 'True', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']"})
        },
        u'mainlab.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
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
        u'mainlab.foldable': {
            'Meta': {'object_name': 'Foldable'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': "'images/pdf.png'", 'max_length': '100'}),
            'instructions': ('tinymce.models.HTMLField', [], {}),
            'purpose': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.grade': {
            'Curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Curriculum']"}),
            'Meta': {'object_name': 'Grade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.graphicorganizer': {
            'Meta': {'object_name': 'GraphicOrganizer'},
            'file': ('django.db.models.fields.files.FileField', [], {'default': "'images/pdf.png'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('tinymce.models.HTMLField', [], {}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mainlab.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'mainlab.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'mainlab.organizer': {
            'Meta': {'object_name': 'Organizer'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'foldables': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Foldable']", 'symmetrical': 'False', 'blank': 'True'}),
            'graphicOrgs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.GraphicOrganizer']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('tinymce.models.HTMLField', [], {}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Link']", 'symmetrical': 'False', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'})
        },
        u'mainlab.project': {
            'Meta': {'object_name': 'Project'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Chapter']", 'symmetrical': 'False'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'foldables': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Foldable']", 'symmetrical': 'False', 'blank': 'True'}),
            'goals': ('tinymce.models.HTMLField', [], {}),
            'graphicOrgs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.GraphicOrganizer']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('tinymce.models.HTMLField', [], {}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainlab.Link']", 'symmetrical': 'False', 'blank': 'True'}),
            'materials': ('tinymce.models.HTMLField', [], {}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'rubric': ('tinymce.models.HTMLField', [], {}),
            'time': ('tinymce.models.HTMLField', [], {}),
            'timeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'timeModified': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'})
        },
        u'mainlab.subject': {
            'Meta': {'object_name': 'Subject'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainlab.Grade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        }
    }

    complete_apps = ['mainlab']