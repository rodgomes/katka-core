# Generated by Django 2.1.5 on 2019-02-15 04:49

import uuid

import django.db.models.deletion
from django.db import migrations, models

import katka.fields


class Migration(migrations.Migration):

    dependencies = [
        ('katka', '0005_scmservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_username', katka.fields.AutoUsernameField(max_length=50)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modified_username', katka.fields.AutoUsernameField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=50)),
                ('public_identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', katka.fields.KatkaSlugField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='katka.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SCMRepository',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_username', katka.fields.AutoUsernameField(max_length=50)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modified_username', katka.fields.AutoUsernameField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=50)),
                ('public_identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('organisation', models.CharField(max_length=128)),
                ('repository_name', models.CharField(max_length=128)),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='katka.Credential')),
                ('scm_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='katka.SCMService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='application',
            name='scm_repository',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='katka.SCMRepository'),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together={('project', 'slug')},
        ),
    ]