from django.urls import path

from .views import signUpView, signInView

urlpatterns = [
    path('signup', signUpView.as_view(), name='signup-page'),
    path('signin', signInView.as_view(), name="signin-page")
]
