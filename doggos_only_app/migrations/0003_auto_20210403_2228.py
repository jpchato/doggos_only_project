# Generated by Django 3.1.4 on 2021-04-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggos_only_app', '0002_dog_dog_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='dog',
            name='demeanor',
            field=models.CharField(blank=True, choices=[('Playful', 'Playful'), ('Nervous', 'Nervous'), ('Anxious', 'Anxious'), ('Excitable', 'Excitable'), ('Patient', 'Patient'), ('Aggressive', 'Aggressive')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='state',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
