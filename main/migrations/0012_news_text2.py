# Generated by Django 3.2.4 on 2021-06-19 10:56

import ckeditor_uploader.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_news_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
