# Generated by Django 3.2.4 on 2021-09-03 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0009_alter_person_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='school_address',
            new_name='school_location',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='company_address',
            new_name='company_location',
        ),
    ]
