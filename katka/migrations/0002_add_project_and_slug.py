# Generated by Django 2.1.5 on 2019-02-07 08:12

import uuid

import django.db.models.deletion
from django.db import migrations, models

import katka.fields


class Migration(migrations.Migration):

    dependencies = [
        ("katka", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("created_username", katka.fields.AutoUsernameField(max_length=50)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("modified_username", katka.fields.AutoUsernameField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "active"), ("inactive", "inactive")], default="active", max_length=50
                    ),
                ),
                (
                    "public_identifier",
                    models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
                ),
                ("slug", katka.fields.KatkaSlugField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="team",
            name="slug",
            field=katka.fields.KatkaSlugField(default="NONE", max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="team",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="katka.Team"),
        ),
    ]
