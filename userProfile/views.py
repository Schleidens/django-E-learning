from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .models import studentProfile, teacherProfile
from .forms import editUserAccountInformationForm, editTeacherProfileForm, deleteAccountForm

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


class editUserAccountInformationView(LoginRequiredMixin, View):
    form_class = editUserAccountInformationForm
    template_class = 'edit_user_account_information_template.html'

    def get(self, request):
        form = self.form_class(instance=request.user)

        return render(request, self.template_class, {'form': form})

    def post(self, request):
        form = self.form_class(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('user-profile-page')

        return render(request, self.template_class, {'form': form})


class editTeacherProfileView(LoginRequiredMixin, View):
    profile_model = teacherProfile
    form_class = editTeacherProfileForm
    template_class = 'edit_teacher_profile_template.html'

    def get(self, request):
        thisTeacherProfile = get_object_or_404(
            teacherProfile, user=request.user)
        form = self.form_class(instance=thisTeacherProfile)

        return render(request, self.template_class, {'form': form})

    def post(self, request):
        thisTeacherProfile = get_object_or_404(
            teacherProfile, user=request.user)
        form = self.form_class(request.POST, instance=thisTeacherProfile)

        if form.is_valid():
            form.save()

            return redirect('user-profile-page')

        return render(request, self.template_class, {'form': form})


# user delete profile view CBVs
class deleteAccountView(LoginRequiredMixin, View):
    delete_form = deleteAccountForm
    template = 'delete_account.html'

    def get(self, request):
        form = self.delete_form()

        return render(request, self.template, {'form': form})

    def post(self, request):
        user = request.user
        user.delete()

        return redirect('signup-page')
