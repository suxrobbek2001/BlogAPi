from django.contrib import admin

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Maqola, Rasm

admin.site.register(Rasm)


@admin.register(Maqola)
class MaqolaAdmin(ModelAdmin):
    search_fields = ['id', 'title', 'matn']
    list_display = ['title', 'matn', 'time']

