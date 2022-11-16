# Generated by Django 3.2.13 on 2022-11-16 02:34

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('reviews', '0003_tagmodel_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]