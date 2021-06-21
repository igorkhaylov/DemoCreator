from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    # slug = models.SlugField("Slug")
    picture = models.ImageField("Картинка", upload_to="media/%Y/%m/%d/")
    content = models.TextField("Контент")
    # text2 = RichTextField()
    # text2 = models.TextField("text")
    # content = RichTextField()
    date = models.DateField("Дата")
    is_published = models.BooleanField("Опубликовать", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date', 'is_published']


class NewsImages(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    post = models.ForeignKey('News', on_delete=models.CASCADE, related_name='images')
    pictures = models.ImageField("Фотографии", upload_to="media/gallery/%Y/%m/%d/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
