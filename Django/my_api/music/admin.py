from django.contrib import admin
from .models import *
# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artist','title')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music, MusicAdmin)