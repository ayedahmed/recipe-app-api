# Generated by Django 2.1.15 on 2020-04-29 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_satff',
            new_name='is_staff',
        ),
    ]
