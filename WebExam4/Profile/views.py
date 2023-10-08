from django.shortcuts import render, redirect

from WebExam4.Album.models import Album
from WebExam4.Profile.forms import ProfileForm, DeleteProfileForm
from WebExam4.Profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def home_page(request):
    # if get_profile() is not None:
    #     return redirect('index')

    profile = Profile.objects.first()
    albums = Album.objects.all()

    if profile is None:
        return redirect('profile-add')

    context = {
        'albums': albums,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def profile_add(request):
    if request.method == "GET":
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-delete.html', context)
