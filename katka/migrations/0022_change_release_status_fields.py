# Generated by Django 2.2.6 on 2019-10-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katka', '0021_added_step_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scmrelease',
            name='status',
            field=models.CharField(choices=[('in progress', 'in progress'), ('failed', 'failed'), ('success', 'success')], default='in progress', max_length=30),
        ),
    ]
