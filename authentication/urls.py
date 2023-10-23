from django.urls import path

from .views import signInView

urlpatterns = [
    path('signin', signInView.as_view(), name='signin')
]
