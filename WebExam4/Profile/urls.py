from django.urls import path

from WebExam4.Profile.views import home_page, profile_details, profile_delete, profile_add

urlpatterns = (
    path('', home_page, name='index'),
    path('add/profile', profile_add, name='profile-add'),
    path('profile/details/', profile_details, name='profile-details'),
    path('profile/delete/', profile_delete, name='profile-delete'),
)