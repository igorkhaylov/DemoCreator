from django.contrib import admin
from .models import News, NewsImages, Schedule, Churches
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class ImagesInline(admin.StackedInline):  # TabularInline
    model = NewsImages
    extra = 1   # сколько полей будет в inlines, default=3


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name="for_church"))

    class Meta:
        model = News
        fields = '__all__'


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


class ChurchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('id', )
    save_on_top = True


admin.site.register(News, NewsAdmin)
admin.site.register(Schedule)
admin.site.register(Churches, ChurchesAdmin)
# admin.site.register(NewsImages, NewsImagesAdmin)


