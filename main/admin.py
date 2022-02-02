from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, NewsImages, Schedule, Churches, MainPagePicture
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class ImagesInline(admin.StackedInline):  # TabularInline
    model = NewsImages
    extra = 10   # сколько полей будет в inlines, default=3


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name="for_church"))

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('date', 'title', 'is_published', 'get_picture')
    prepopulated_fields = {'slug': ('title', )}
    list_display_links = ('date', 'title')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    readonly_fields = ('views', 'get_picture')
    inlines = [
        ImagesInline,
    ]
    save_on_top = True  # Поле сохранить будет вверху
    save_as = True  # сохранить как новый объект

    def get_picture(self, obj):
        if obj.picture:  # если есть фото
            return mark_safe(f"<img src=\"{obj.picture.url}\" width=\"50\"")
        return "-"  # если нет фото, возвращаем такую строку

    get_picture.short_description = "Фото"


class NewsImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class ChurchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('id', )
    save_on_top = True


@admin.register(MainPagePicture)
class MainPagePictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_picture')
    list_display_links = ('name', )
    save_on_top = True

    def get_picture(self, obj):
        if obj.picture: # если есть фото
            return mark_safe(f"<img src=\"{obj.picture.url}\" width=\"100\"")
        return "-" # если нет фото, возвращаем такую строку

    get_picture.short_description = "Фото"


admin.site.register(News, NewsAdmin)
admin.site.register(Schedule)
# admin.site.register(MainPagePicture)
admin.site.register(Churches, ChurchesAdmin)
# admin.site.register(NewsImages, NewsImagesAdmin)

admin.site.site_title = "Управление сайтом"
admin.site.site_header = "Свято-Алексеевский Собор"



'''how's life what are you doing Svetlana, i think, i Love you, i need you'''
