from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'completed', 'author_id', 'created_at', 'updated_at',)

admin.site.register(Todo, TodoAdmin)
