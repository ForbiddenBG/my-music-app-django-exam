from django.contrib import admin

from WebExam4.Album.models import Album


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
