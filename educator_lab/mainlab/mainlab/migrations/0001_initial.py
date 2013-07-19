# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyUser'
        db.create_table(u'mainlab_myuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mainlab', ['MyUser'])

        # Adding model 'Curriculum'
        db.create_table(u'mainlab_curriculum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Curriculum'])

        # Adding model 'Grade'
        db.create_table(u'mainlab_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Curriculum'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mainlab', ['Grade'])

        # Adding model 'Subject'
        db.create_table(u'mainlab_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Grade'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Subject'])

        # Adding model 'Chapter'
        db.create_table(u'mainlab_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Subject'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mainlab', ['Chapter'])

        # Adding model 'File'
        db.create_table(u'mainlab_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('doc', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['File'])

        # Adding model 'Link'
        db.create_table(u'mainlab_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Link'])

        # Adding model 'Item'
        db.create_table(u'mainlab_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'mainlab', ['Item'])

        # Adding model 'Foldable'
        db.create_table(u'mainlab_foldable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
            ('purpose', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default='images/pdf.png', max_length=100)),
        ))
        db.send_create_signal(u'mainlab', ['Foldable'])

        # Adding model 'GraphicOrganizer'
        db.create_table(u'mainlab_graphicorganizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('file', self.gf('django.db.models.fields.files.FileField')(default='images/pdf.png', max_length=100)),
        ))
        db.send_create_signal(u'mainlab', ['GraphicOrganizer'])

        # Adding model 'Activity'
        db.create_table(u'mainlab_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('goals', self.gf('tinymce.models.HTMLField')()),
            ('time', self.gf('tinymce.models.HTMLField')()),
            ('materials', self.gf('tinymce.models.HTMLField')()),
            ('lesson', self.gf('tinymce.models.HTMLField')()),
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('timeModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Activity'])

        # Adding M2M table for field chapters on 'Activity'
        db.create_table(u'mainlab_activity_chapters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('chapter', models.ForeignKey(orm[u'mainlab.chapter'], null=False))
        ))
        db.create_unique(u'mainlab_activity_chapters', ['activity_id', 'chapter_id'])

        # Adding M2M table for field links on 'Activity'
        db.create_table(u'mainlab_activity_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_activity_links', ['activity_id', 'link_id'])

        # Adding M2M table for field files on 'Activity'
        db.create_table(u'mainlab_activity_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('file', models.ForeignKey(orm[u'mainlab.file'], null=False))
        ))
        db.create_unique(u'mainlab_activity_files', ['activity_id', 'file_id'])

        # Adding M2M table for field items on 'Activity'
        db.create_table(u'mainlab_activity_items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('item', models.ForeignKey(orm[u'mainlab.item'], null=False))
        ))
        db.create_unique(u'mainlab_activity_items', ['activity_id', 'item_id'])

        # Adding M2M table for field foldables on 'Activity'
        db.create_table(u'mainlab_activity_foldables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('foldable', models.ForeignKey(orm[u'mainlab.foldable'], null=False))
        ))
        db.create_unique(u'mainlab_activity_foldables', ['activity_id', 'foldable_id'])

        # Adding M2M table for field graphicOrgs on 'Activity'
        db.create_table(u'mainlab_activity_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'mainlab.activity'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_activity_graphicOrgs', ['activity_id', 'graphicorganizer_id'])

        # Adding model 'Project'
        db.create_table(u'mainlab_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('goals', self.gf('tinymce.models.HTMLField')()),
            ('time', self.gf('tinymce.models.HTMLField')()),
            ('materials', self.gf('tinymce.models.HTMLField')()),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
            ('rubric', self.gf('tinymce.models.HTMLField')()),
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('timeModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Project'])

        # Adding M2M table for field chapters on 'Project'
        db.create_table(u'mainlab_project_chapters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('chapter', models.ForeignKey(orm[u'mainlab.chapter'], null=False))
        ))
        db.create_unique(u'mainlab_project_chapters', ['project_id', 'chapter_id'])

        # Adding M2M table for field links on 'Project'
        db.create_table(u'mainlab_project_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_project_links', ['project_id', 'link_id'])

        # Adding M2M table for field files on 'Project'
        db.create_table(u'mainlab_project_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('file', models.ForeignKey(orm[u'mainlab.file'], null=False))
        ))
        db.create_unique(u'mainlab_project_files', ['project_id', 'file_id'])

        # Adding M2M table for field foldables on 'Project'
        db.create_table(u'mainlab_project_foldables', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('foldable', models.ForeignKey(orm[u'mainlab.foldable'], null=False))
        ))
        db.create_unique(u'mainlab_project_foldables', ['project_id', 'foldable_id'])

        # Adding M2M table for field graphicOrgs on 'Project'
        db.create_table(u'mainlab_project_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'mainlab.project'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_project_graphicOrgs', ['project_id', 'graphicorganizer_id'])

        # Adding model 'Organizer'
        db.create_table(u'mainlab_organizer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('titleTag', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('instructions', self.gf('tinymce.models.HTMLField')()),
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('timeModified', self.gf('django.db.models.fields.DateTimeField')()),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'mainlab', ['Organizer'])

        # Adding M2M table for field chapters on 'Organizer'
        db.create_table(u'mainlab_organizer_chapters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('chapter', models.ForeignKey(orm[u'mainlab.chapter'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_chapters', ['organizer_id', 'chapter_id'])

        # Adding M2M table for field links on 'Organizer'
        db.create_table(u'mainlab_organizer_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('link', models.ForeignKey(orm[u'mainlab.link'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_links', ['organizer_id', 'link_id'])

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

        # Adding M2M table for field graphicOrgs on 'Organizer'
        db.create_table(u'mainlab_organizer_graphicOrgs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizer', models.ForeignKey(orm[u'mainlab.organizer'], null=False)),
            ('graphicorganizer', models.ForeignKey(orm[u'mainlab.graphicorganizer'], null=False))
        ))
        db.create_unique(u'mainlab_organizer_graphicOrgs', ['organizer_id', 'graphicorganizer_id'])

        # Adding model 'Comment'
        db.create_table(u'mainlab_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Activity'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Project'], null=True, blank=True)),
            ('organizer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.Organizer'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainlab.MyUser'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('timeCreated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'mainlab', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'MyUser'
        db.delete_table(u'mainlab_myuser')

        # Deleting model 'Curriculum'
        db.delete_table(u'mainlab_curriculum')

        # Deleting model 'Grade'
        db.delete_table(u'mainlab_grade')

        # Deleting model 'Subject'
        db.delete_table(u'mainlab_subject')

        # Deleting model 'Chapter'
        db.delete_table(u'mainlab_chapter')

        # Deleting model 'File'
        db.delete_table(u'mainlab_file')

        # Deleting model 'Link'
        db.delete_table(u'mainlab_link')

        # Deleting model 'Item'
        db.delete_table(u'mainlab_item')

        # Deleting model 'Foldable'
        db.delete_table(u'mainlab_foldable')

        # Deleting model 'GraphicOrganizer'
        db.delete_table(u'mainlab_graphicorganizer')

        # Deleting model 'Activity'
        db.delete_table(u'mainlab_activity')

        # Removing M2M table for field chapters on 'Activity'
        db.delete_table('mainlab_activity_chapters')

        # Removing M2M table for field links on 'Activity'
        db.delete_table('mainlab_activity_links')

        # Removing M2M table for field files on 'Activity'
        db.delete_table('mainlab_activity_files')

        # Removing M2M table for field items on 'Activity'
        db.delete_table('mainlab_activity_items')

        # Removing M2M table for field foldables on 'Activity'
        db.delete_table('mainlab_activity_foldables')

        # Removing M2M table for field graphicOrgs on 'Activity'
        db.delete_table('mainlab_activity_graphicOrgs')

        # Deleting model 'Project'
        db.delete_table(u'mainlab_project')

        # Removing M2M table for field chapters on 'Project'
        db.delete_table('mainlab_project_chapters')

        # Removing M2M table for field links on 'Project'
        db.delete_table('mainlab_project_links')

        # Removing M2M table for field files on 'Project'
        db.delete_table('mainlab_project_files')

        # Removing M2M table for field foldables on 'Project'
        db.delete_table('mainlab_project_foldables')

        # Removing M2M table for field graphicOrgs on 'Project'
        db.delete_table('mainlab_project_graphicOrgs')

        # Deleting model 'Organizer'
        db.delete_table(u'mainlab_organizer')

        # Removing M2M table for field chapters on 'Organizer'
        db.delete_table('mainlab_organizer_chapters')

        # Removing M2M table for field links on 'Organizer'
        db.delete_table('mainlab_organizer_links')

        # Removing M2M table for field files on 'Organizer'
        db.delete_table('mainlab_organizer_files')

        # Removing M2M table for field foldables on 'Organizer'
        db.delete_table('mainlab_organizer_foldables')

        # Removing M2M table for field graphicOrgs on 'Organizer'
        db.delete_table('mainlab_organizer_graphicOrgs')

        # Deleting model 'Comment'
        db.delete_table(u'mainlab_comment')


    models = {
        u'mainlab.activity': {
            'Meta': {'object_name': 'Activity'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
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
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
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
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'mainlab.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainlab.MyUser']", 'null': 'True', 'blank': 'True'}),
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
            'titleTag': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
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