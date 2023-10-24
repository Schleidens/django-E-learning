from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

from django.http import HttpResponse


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
            login(request, user)

            return redirect("home-page")
        return render(request, self.template, {"form": form})


# login user

class signInView(View):
    template = "signin.html"
    class_form = signInUserForm

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

            if user is not None:
                login(request, user)

                return redirect("home-page")

        return render(request, self.template, {"form": form})
