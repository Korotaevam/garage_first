from django.contrib import admin

from .models import *


class AutoModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'articles', 'group', 'slug', 'subgroup', 'photo', 'is_published')
    list_display_links = ('articles', 'group')
    search_fields = ('articles', 'group')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'group')
    prepopulated_fields = {'slug': ('group', 'subgroup', 'auto_model')}


class ModelAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id',)


admin.site.register(AutoModels, AutoModelsAdmin)
admin.site.register(ModelAdd, ModelAddAdmin)
admin.site.register(GroupAdd)
admin.site.register(SubGroupAdd)
