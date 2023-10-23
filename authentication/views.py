from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login

from .forms import createUserForm

# Create your views here.


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
