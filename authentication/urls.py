from django.urls import path

from .views import signUpView, signInView, LogoutView, newTeacherMessageView, changePasswordView

urlpatterns = [
    path('signup', signUpView.as_view(), name='signup-page'),
    path('signin', signInView.as_view(), name="signin-page"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('new-teacher', newTeacherMessageView, name="new-teacher-page"),
    path('change-password', changePasswordView.as_view(), name='change-password')
]
