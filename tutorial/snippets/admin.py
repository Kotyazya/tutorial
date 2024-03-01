from django.contrib import admin
from .models import Snippet
# Обновили Админ

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ("highlighted",)


admin.site.register(Snippet, SnippetAdmin)