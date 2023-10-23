from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class signInView(View):
    template = 'signin.html'

    def get(self, request):
        return render(request, self.template)
