# Generated by Django 3.2.6 on 2022-02-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20220113_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='churches',
            name='keywords_meta',
            field=models.TextField(null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='news',
            name='keywords_meta',
            field=models.TextField(null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='keywords_meta',
            field=models.TextField(null=True, verbose_name='Ключевые слова'),
        ),
    ]
