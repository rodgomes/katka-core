# Generated by Django 2.2.9 on 2020-03-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("katka", "0032_added_step_aborted"),
    ]

    operations = [
        migrations.AddField(model_name="scmpipelinerun", name="output", field=models.TextField(blank=True),),
    ]
