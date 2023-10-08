from django.urls import path

from WebExam4.Album.views import album_add, album_details, album_edit, album_delete

urlpatterns = (
    path('album/add/', album_add, name='album-add'),
    path('album/details/<int:id>/', album_details, name='album-details'),
    path('album/edit/<int:id>/', album_edit, name='album-edit'),
    path('album/delete/<int:id>/', album_delete, name='album-delete'),
)
