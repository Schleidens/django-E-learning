from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.db import transaction

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .forms import createUserForm, signInUserForm, changePasswordForm
from userProfile.models import studentProfile, teacherProfile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash


class signUpView(View):
    template = 'signup.html'
    class_form = createUserForm
    student_profile_model = studentProfile
    teacher_profile_model = teacherProfile

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home-page")
        else:
            form = self.class_form()

        return render(request, self.template, {"form": form})

    @transaction.atomic
    def post(self, request):
        form = self.class_form(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            if user.is_teacher:
                user.is_active = False
            else:
                user.is_active = True

            user.save()
            login(request, user)

            if user.is_teacher:
                profile_model = self.teacher_profile_model
                redirect_url = "new-teacher-page"
            else:
                profile_model = self.student_profile_model
                redirect_url = "home-page"

            profile, created = profile_model.objects.get_or_create(user=user)
            return redirect(redirect_url)

        return render(request, self.template, {"form": form})


# login user

class signInView(View):
    template = "signin.html"
    class_form = signInUserForm
    message = ''

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home-page")
        else:
            form = self.class_form()

        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None and user.is_active:
                login(request, user)
                return redirect("home-page")
            else:
                self.message = 'credentials invalid'

            context = {
                "form": form,
                'message': self.message
            }

        return render(request, self.template, context=context)


# change password view CBVs
class changePasswordView(LoginRequiredMixin, View):
    password_form = changePasswordForm
    template = 'change_password.html'

    def get(self, request):
        form = self.password_form(request.user)

        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.password_form(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return redirect('user-profile-page')

        return render(request, self.template, {'form': form})


# logout view CBVs
class user_logout_view(LogoutView):
    next_page = reverse_lazy('home-page')


# page for suspended users
def newTeacherMessageView(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    else:
        return render(request, 'new-teacher.html')
