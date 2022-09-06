# Generated by Django 3.1.1 on 2020-10-24 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('lecturer', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('credit', models.CharField(max_length=10)),
                ('term', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='EventsParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('eventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story_one.events')),
            ],
        ),
    ]
