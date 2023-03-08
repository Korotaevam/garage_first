from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AutoModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'articles', 'group', 'slug', 'subgroup', 'photo', 'get_html_photo', 'is_published')
    list_display_links = ('articles', 'group')
    search_fields = ('articles', 'group')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'group')
    prepopulated_fields = {'slug': ('group', 'subgroup', 'auto_model')}
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    fields = ('articles', 'slug', 'group', 'subgroup', 'auto_model', 'time_create', 'time_update', 'photo', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50>')

    get_html_photo.short_description = 'Photo'


class ModelAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id',)


admin.site.register(AutoModels, AutoModelsAdmin)
admin.site.register(ModelAdd, ModelAddAdmin)
admin.site.register(GroupAdd)
admin.site.register(SubGroupAdd)

admin.site.site_header = 'Auto Models Admin'
admin.site.site_title = 'Auto Models Admin'
