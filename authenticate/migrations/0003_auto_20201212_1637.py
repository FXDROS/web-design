# Generated by Django 3.1.1 on 2020-12-12 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_auto_20201208_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='photo',
        ),
    ]
