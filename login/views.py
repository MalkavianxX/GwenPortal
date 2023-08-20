from django.shortcuts import render
from curso.models import Curso, Taller

# Create your views here.
def login(request):
    cursos = Curso.objects.all().order_by('-id')[:5]
    talleres = Taller.objects.all().order_by('-id')[:5]
    return render(request,"login/login.html",{
        'cursos': cursos, 
        'talleres':talleres,
    })