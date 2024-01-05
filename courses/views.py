from django.shortcuts import render, redirect

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
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            course = form.save(commit=False)

            course.author = request.user
            course.save()

            return redirect('home-page')

        return render(request, self.template, {'form': self.form_class})
