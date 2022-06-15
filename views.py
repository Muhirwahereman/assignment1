from django.shortcuts import render
from portifolio.models import Project

# Create your views here.
def index(request):
    works = Project.objects.all
    work = {'works': works, }
    return render(request, 'index.html', work)


def details(request, pk):
    works = Project.objects.get(pk=pk)
    works= {'works': works, }
    return render(request, 'details.html', works)