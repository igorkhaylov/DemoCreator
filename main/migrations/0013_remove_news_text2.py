# Generated by Django 3.2.4 on 2021-06-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_news_text2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='text2',
        ),
    ]
