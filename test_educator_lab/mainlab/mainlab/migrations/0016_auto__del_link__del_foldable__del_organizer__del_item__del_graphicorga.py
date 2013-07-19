# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'mainlab_link')

        # Deleting model 'Foldable'
        db.delete_table(u'mainlab_foldable')

        # Deleting model 'Organizer'
        db.delete_table(u'mainlab_organizer')

        # Removing M2M table for field files on 'Organizer'
        db.delete_table('mainlab_organizer_files')

        # Removing M2M table for field foldables on 'Organizer'
        db.delete_table('mainlab_organizer_foldables')

        # Removing M2M table for field links on 'Organizer'
        db.delete_table('mainlab_organizer_links')

        # Removing M2M table for field chapters on 'Organizer'
        db.delete_table('mainlab_organizer_chapters')

        # Removing M2M table for field graphicOrgs on 'Organizer'
        db.delete_table('mainlab_organizer_graphicOrgs')

        # Deleting model 'Item'
        db.delete_table(u'mainlab_item')

        # Deleting model 'GraphicOrganizer'
        db.delete_table(u'mainlab_graphicorganizer')

        # Removing M2M table for field links on 'Project'
        db.delete_table('mainlab_project_links')

        # Removing M2M table for field graphicOrgs on 'Project'
        db.delete_table('mainlab_project_graphicOrgs')

        # Removing M2M table for field foldables on 'Project'
        db.delete_table('mainlab_project_foldables')

        # Removing M2M table for field links on 'Activity'
        db.delete_table('mainlab_activity_links')

        # Removing M2M table for field graphicOrgs on 'Activity'
        db.delete_table('mainlab_activity_graphicOrgs')

        # Removing M2M table for field foldables on 'Activity'
        db.delete_table('mainlab_activity_foldables')

        # Removing M2M table for field items on 'Activity'
        db.delete_table('mainlab_activity_items')

        # Deleting field 'Comment.organizer'
        db.delete_column(u'mainlab_comment', 'organizer_id')


    def backwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'mainlab_link', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mainlab', ['Link'])

        # Adding model 'Foldable'
        db.create_table(u'mainlab_foldable', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='foldables/pdf.png', max_length=100)),
            ('purpose', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'mainlab', ['Foldable'])

        # Adding model 'Organizer'
        db.create_table(u'mainlab_organizer', (
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('userModified', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['mainlab.MyUser'], blank=True)),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'mainlab', ['Organizer'])

        # Adding M2M table for field files on 'Organizer'
        db.create_table(u'mainlab_organizer_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('file', models.ForeignKey(orm[u'mainlab.file'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_files', ['organizer_id', 'file_id'])

        # Adding M2M table for field foldables on 'Organizer'
        db.create_table(u'mainlab_organizer_foldables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('foldable', models.ForeignKey(orm[u'mainlab.foldable'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_foldables', ['organizer_id', 'foldable_id'])

        # Adding M2M table for field links on 'Organizer'
        db.create_table(u'mainlab_organizer_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_links', ['organizer_id', 'link_id'])

        # Adding M2M table for field chapters on 'Organizer'
        db.create_table(u'mainlab_organizer_chapters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('chapter', models.ForeignKey(orm[u'mainlab.chapter'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_chapters', ['organizer_id', 'chapter_id'])

        # Adding M2M table for field graphicOrgs on 'Organizer'
        db.create_table(u'mainlab_organizer_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_graphicOrgs', ['organizer_id', 'graphicorganizer_id'])

        # Adding model 'Item'
        db.create_table(u'mainlab_item', (
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'mainlab', ['Item'])

        # Adding model 'GraphicOrganizer'
        db.create_table(u'mainlab_graphicorganizer', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('file', self.gf('django.db.models.fields.files.FileField')(default='graphicOrgs/pdf.png', max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'mainlab', ['GraphicOrganizer'])

        # Adding M2M table for field links on 'Project'
        db.create_table(u'mainlab_project_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_project_links', ['project_id', 'link_id'])

        # Adding M2M table for field graphicOrgs on 'Project'
        db.create_table(u'mainlab_project_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_project_graphicOrgs', ['project_id', 'graphicorganizer_id'])

        # Adding M2M table for field foldables on 'Project'
        db.create_table(u'mainlab_project_foldables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('foldable', models.ForeignKey(orm[u'mainlab.foldable'], null=False))
        ))
        db.create_unique(u'mainlab_project_foldables', ['project_id', 'foldable_id'])

        # Adding M2M table for field links on 'Activity'
        db.create_table(u'mainlab_activity_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_activity_links', ['activity_id', 'link_id'])

        # Adding M2M table for field graphicOrgs on 'Activity'
        db.create_table(u'mainlab_activity_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_activity_graphicOrgs', ['activity_id', 'graphicorganizer_id'])

        # Adding M2M table for field foldables on 'Activity'
        db.create_table(u'mainlab_activity_foldables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('foldable', models.ForeignKey(orm[u'mainlab.foldable'], null=False))
        ))
        db.create_unique(u'mainlab_activity_foldables', ['activity_id', 'foldable_id'])

        # Adding M2M table for field items on 'Activity'
        db.create_table(u'mainlab_activity_items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('item', models.ForeignKey(orm[u'mainlab.item'], null=False))
        ))
        db.create_unique(u'mainlab_activity_items', ['activity_id', 'item_id'])

        # Adding field 'Comment.organizer'
        db.add_column(u'mainlab_comment', 'organizer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Organizer'], null=True, blank=True),
                      keep_default=False)


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
            'time': ('tinymce.models.HTMLField', [], {}),
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
            'rubric': ('tinymce.models.HTMLField', [], {}),
            'time': ('tinymce.models.HTMLField', [], {}),
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
        }
    }

    complete_apps = ['mainlab']