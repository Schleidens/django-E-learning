from django.urls import path

from .views import homeView, userProfileView

urlpatterns = [
    path('', homeView, name='home-page'),
    path('profile', userProfileView.as_view(), name='user-profile-page'),
]
