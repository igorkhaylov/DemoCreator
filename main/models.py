from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class MainPagePicture(models.Model):
    name = models.CharField("Название картинки", max_length=50, null=True, blank=False)
    picture = models.ImageField("Картинка 1770x742", upload_to="mainPicture/")
    title = models.CharField("Заголовок (не обязательно)", max_length=50, null=True, blank=True)
    description = models.CharField("Описание (мелкий текст)", max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главная картинка страницы"
        verbose_name_plural = "Главные картинки страниц"
        ordering = ["id", ]


class News(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    slug = models.SlugField("slug", max_length=40)
    picture = models.ImageField("Картинка", upload_to="articles/%Y/%m/%d/")
    keywords_meta = models.TextField("Ключевые слова", null=True, blank=True)
    content = models.TextField("Контент")
    date = models.DateField("Дата")
    is_published = models.BooleanField("Опубликовать", default=True)
    views = models.PositiveIntegerField("Просмотры", default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("post_detail", kwargs={"pk": self.pk})
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date', 'is_published']


class NewsImages(models.Model):
    title = models.CharField(max_length=150, db_index=True, default="image")
    post = models.ForeignKey('News', on_delete=models.CASCADE, related_name='images')
    pictures = models.ImageField("Фотографии", upload_to="media/gallery/%Y/%m/%d/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Schedule(models.Model):
    keywords_meta = models.TextField("Ключевые слова", null=True, blank=True)
    schedule = RichTextField("Богослужения", config_name="schedule")

    def __str__(self):
        return "Богослужения"

    class Meta:
        verbose_name = "Богослужения"
        verbose_name_plural = "Богослужения"


class Churches(models.Model):
    name = models.CharField("Название", max_length=70)
    slug = models.SlugField("Slug")
    picture = models.ImageField("Фотография", upload_to="media/churches")
    keywords_meta = models.TextField("Ключевые слова", null=True, blank=True)
    short_text = models.TextField("Короткое описание", max_length=350)
    content = RichTextUploadingField("Описание", config_name="for_church")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Храм"
        verbose_name_plural = "Храмы"
        ordering = ["id"]


