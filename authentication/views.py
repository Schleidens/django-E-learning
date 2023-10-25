from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .forms import createUserForm, signInUserForm


class signUpView(View):
    template = 'signup.html'
    class_form = createUserForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home-page")
        else:
            form = self.class_form()

        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)

        if form.is_valid():
            user = form.save()

            if user.is_teacher:
                user.is_active = False
                user.save()
                return redirect("new-teacher-page")
            else:
                user.is_active = True
                user.save()
                login(request, user)
                return redirect("home-page")

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


# logout view CBVs
class user_logout_view(LogoutView):
    next_page = reverse_lazy('home-page')


# page for suspended users
# @login_required
def newTeacherMessageView(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    else:
        return render(request, 'new-teacher.html')
