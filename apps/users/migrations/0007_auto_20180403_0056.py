# Generated by Django 2.0.3 on 2018-04-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180402_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
    ]