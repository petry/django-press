# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Article.section'
        db.add_column(u'press_article', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          default=1, to=orm['press.Section']),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Article.section'
        db.delete_column(u'press_article', 'section_id')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '80'}),
            'permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['auth.Permission']", 'symmetrical': 'False',
             'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {
            'ordering': "(u'content_type__app_label', "
                        "u'content_type__model', u'codename')",
            'unique_together': "((u'content_type', u'codename'),)",
            'object_name': 'Permission'},
            'codename': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': u"orm['contenttypes.ContentType']"}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [],
                            {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [],
                      {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [],
                           {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'to': u"orm['auth.Group']", 'symmetrical': 'False',
                        'blank': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [],
                           {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [],
                          {'max_length': '30', 'blank': 'True'}),
            'password': (
            'django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['auth.Permission']", 'symmetrical': 'False',
             'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [],
                         {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)",
                     'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType',
                     'db_table': "'django_content_type'"},
            'app_label': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'press.article': {
            'Meta': {
                'ordering': "['modified_date']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['press.Author']", 'null': 'True',
                        'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {
                'default': 'datetime.datetime(2013, 6, 18, 0, 0)',
                'auto_now_add': 'True', 'blank': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [],
                          {'default': 'False', 'db_index': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {
            'default': 'datetime.datetime(2013, 6, 18, 0, 0)',
            'auto_now': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.OneToOneField', [],
                       {'related_name': "'draft'", 'unique': 'True',
                        'null': 'True', 'to': u"orm['press.Article']"}),
            'publish_state': ('django.db.models.fields.IntegerField', [],
                              {'default': '0', 'db_index': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['press.Section']"}),
            'slug': ('django.db.models.fields.CharField', [],
                     {'max_length': '100', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [],
                         {'max_length': '500', 'blank': 'True'}),
            'title': (
            'django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'to': u"orm['auth.User']"})
        },
        u'press.author': {
            'Meta': {'ordering': "['user__first_name', 'user__last_name']",
                     'object_name': 'Author'},
            'about': ('django.db.models.fields.TextField', [], {}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'to': u"orm['auth.User']"})
        },
        u'press.section': {
            'Meta': {'object_name': 'Section'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['press']
