# Generated by Django 2.0.3 on 2018-03-27 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20180327_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='student',
            new_name='students',
        ),
    ]
