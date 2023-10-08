from django.shortcuts import render, redirect

from WebExam4.Album.forms import AlbumForm, DeleteAlbumForm
from WebExam4.Album.models import Album
from WebExam4.Profile.views import get_profile


# Create your views here.
def album_add(request):
    profile = get_profile()

    if request.method == "GET":
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-album.html', context)


def album_details(request, id):
    album = Album.objects.get(pk=id)
    profile = get_profile()

    context = {
        'album': album,
        'profile': profile,
    }

    return render(request, 'album-details.html', context)


def album_edit(request, id):
    album = Album.objects.get(pk=id)
    profile = get_profile()

    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'album': album,
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-album.html', context)


def album_delete(request, id):
    album = Album.objects.get(pk=id)
    profile = get_profile()

    if request.method == "GET":
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'album': album,
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-album.html', context)
