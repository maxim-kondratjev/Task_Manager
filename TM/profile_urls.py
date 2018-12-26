from django.urls import path

from TM.views import ProfileView, UpdateProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('update/', UpdateProfileView.as_view(), name='profile_update')
]