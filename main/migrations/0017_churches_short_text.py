# Generated by Django 3.2.4 on 2021-06-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_churches_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='churches',
            name='short_text',
            field=models.CharField(default='some short text', max_length=350, verbose_name='Короткое описание'),
            preserve_default=False,
        ),
    ]
