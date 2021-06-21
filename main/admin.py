from django.contrib import admin
from .models import News, NewsImages
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget



class ImagesInline(admin.StackedInline):
# class ImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 1   # сколько полей будет в inlines, default=3


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name="for_church"))

    class Meta:
        model = News
        fields = '__all__'


# @admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('date', 'title', 'is_published')
    list_display_links = ('date', 'title')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    inlines = [
        ImagesInline,
    ]
    save_on_top = True  # Поле сохранить будет вверху


class NewsImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(News, NewsAdmin)
# admin.site.register(NewsImages, NewsImagesAdmin)


