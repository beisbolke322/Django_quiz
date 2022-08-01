from django.shortcuts import render
from django.views import View
from .models import Generatorius

# Create your views here.


class Klausimai(View):
    model = Generatorius
    template_name = 'quiz.html'

    def get(self, request):
        x = Generatorius.objects.all()
        return render(request, self.template_name, {'x': x})
