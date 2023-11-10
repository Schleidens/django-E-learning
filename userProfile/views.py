from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .models import studentProfile, teacherProfile

# Create your views here.


def homeView(request):
    return render(request, 'home.html')


class userProfileView(LoginRequiredMixin, View):
    student_profile_model = studentProfile
    teacher_profile_model = teacherProfile
    template = ''

    def get(self, request):
        if request.user.is_teacher:
            model = self.teacher_profile_model
            template = 'teacher_profile_template.html'
        else:
            model = self.student_profile_model
            template = 'student_profile_template.html'

        profile = get_object_or_404(model, user=request.user)

        return render(request, template, {'profile': profile})

    def post(self, request):
        pass
