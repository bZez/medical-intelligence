# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.utils import timezone


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DiscussionMember'
        db.create_table(u'messaging_discussionmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('join', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.MedintUser'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'messaging', ['DiscussionMember'])

        # Adding field 'Discussion.starter'
        db.add_column(u'messaging_discussion', 'starter',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_discussion', null=True, to=orm['messaging.DiscussionMember']),
                      keep_default=False)

        # Adding M2M table for field participants on 'Discussion'
        db.create_table(u'messaging_discussion_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('discussion', models.ForeignKey(orm[u'messaging.discussion'], null=False)),
            ('discussionmember', models.ForeignKey(orm[u'messaging.discussionmember'], null=False))
        ))
        db.create_unique(u'messaging_discussion_participants', ['discussion_id', 'discussionmember_id'])
        now = timezone.now()
        for d in orm['messaging.Discussion'].objects.all():
            if 0 < len(d.discussionmessage_set.all()):
                starter, join = d.discussionmessage_set.all()[0].sender, d.discussionmessage_set.all()[0].sent
                ds = orm['messaging.DiscussionMember'].objects.create(user=starter, join=join)
                d.starter = ds
                for m in d.members.all():
                    if m.id != starter.id:
                        print 'add %s (%s)' % (m.username, starter.username)
                        d.participants.add(orm['messaging.DiscussionMember'].objects.create(user=m, join=now))
                d.save()


    def backwards(self, orm):
        # Deleting model 'DiscussionMember'
        db.delete_table(u'messaging_discussionmember')

        # Deleting field 'Discussion.starter'
        db.delete_column(u'messaging_discussion', 'starter_id')

        # Removing M2M table for field participants on 'Discussion'
        db.delete_table('messaging_discussion_participants')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'common.medintuser': {
            'Meta': {'object_name': 'MedintUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.IntegerField', [], {}),
            'user_info': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user'", 'unique': 'True', 'null': 'True', 'to': u"orm['common.UserInfo']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'common.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'messaging.contactitem': {
            'Meta': {'object_name': 'ContactItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['common.MedintUser']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_contacts'", 'to': u"orm['common.MedintUser']"})
        },
        u'messaging.discussion': {
            'Meta': {'object_name': 'Discussion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['common.MedintUser']", 'symmetrical': 'False'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['messaging.DiscussionMember']", 'symmetrical': 'False'}),
            'starter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_discussion'", 'null': 'True', 'to': u"orm['messaging.DiscussionMember']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'messaging.discussionaccess': {
            'Meta': {'object_name': 'DiscussionAccess'},
            'access_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1969, 12, 31, 0, 0)'}),
            'discussion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['messaging.Discussion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.MedintUser']"})
        },
        u'messaging.discussionfolder': {
            'Meta': {'object_name': 'DiscussionFolder'},
            'discussions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['messaging.Discussion']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.MedintUser']"})
        },
        u'messaging.discussionmember': {
            'Meta': {'object_name': 'DiscussionMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'join': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.MedintUser']"})
        },
        u'messaging.discussionmessage': {
            'Meta': {'ordering': "['sent']", 'object_name': 'DiscussionMessage'},
            'discussion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['messaging.Discussion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_messages'", 'to': u"orm['common.MedintUser']"}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['messaging']