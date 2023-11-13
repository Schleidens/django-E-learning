from django.urls import path

from .views import homeView, userProfileView, editUserAccountInformationView

urlpatterns = [
    path('', homeView, name='home-page'),
    path('profile', userProfileView.as_view(), name='user-profile-page'),
    path('profile/edit', editUserAccountInformationView.as_view(),
         name='edit-account-info-page'),
]
