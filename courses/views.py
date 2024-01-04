from django.shortcuts import render

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import coursesForm

# Create your views here.


class coursesView(LoginRequiredMixin, View):
    form_class = coursesForm
    template = 'courses_intro_template.html'

    def get(self, request):

        return render(request, self.template, {'form': self.form_class})

    def post(self, request):
        pass
