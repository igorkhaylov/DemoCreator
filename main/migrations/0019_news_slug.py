# Generated by Django 3.2.4 on 2021-07-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210706_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
    ]