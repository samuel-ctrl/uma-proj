# Generated by Django 3.2.4 on 2021-09-25 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0014_auto_20210924_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='behance_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='codepen_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='dribble_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='figma_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='github_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
