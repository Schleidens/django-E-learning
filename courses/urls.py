from django.urls import path

from .views import createNewCoursesView, allCoursesListView

urlpatterns = [
    path('courses/new', createNewCoursesView.as_view(), name='new-courses-pages'),
    path('courses', allCoursesListView.as_view(), name='courses-pages'),
]
