from django.urls import path

from .views import homeView, userProfileView, editUserAccountInformationView, editTeacherProfileView, deleteAccountView

urlpatterns = [
    path('', homeView, name='home-page'),
    path('profile', userProfileView.as_view(), name='user-profile-page'),
    path('account-info/edit', editUserAccountInformationView.as_view(),
         name='edit-account-info-page'),
    path('profile/edit', editTeacherProfileView.as_view(),
         name='user-profile-edit-page'),
    path('account/delete', deleteAccountView.as_view(),
         name='delete-account'),
]
