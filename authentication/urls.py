from django.urls import path

from .views import signUpView, signInView, LogoutView, newTeacherMessageView

urlpatterns = [
    path('signup', signUpView.as_view(), name='signup-page'),
    path('signin', signInView.as_view(), name="signin-page"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('new-teacher', newTeacherMessageView, name="new-teacher-page"),
]
