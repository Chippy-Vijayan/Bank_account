# Generated by Django 4.2.8 on 2024-01-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
