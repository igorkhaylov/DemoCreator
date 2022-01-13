# Generated by Django 3.2.6 on 2022-01-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPagePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='mainPicture/', verbose_name='Картинка 1770x742')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок (не обязательно)')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание (мелкий текст)')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(upload_to='articles/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
