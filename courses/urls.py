from django.urls import path

from .views import coursesView

urlpatterns = [
    path('courses', coursesView.as_view(), name='courses-pages'),
]
