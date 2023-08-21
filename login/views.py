from django.shortcuts import render
from curso.models import Curso, Taller
from inicio_sesion.models import Comentario
# Create your views here.
def login(request):
    cursos = Curso.objects.all().order_by('-id')[:5]
    talleres = Taller.objects.all().order_by('-id')[:5]
    comms = Comentario.objects.filter(estatus = True).order_by('-fecha')
    return render(request,"login/login.html",{
        'cursos': cursos, 
        'talleres':talleres,
        'comms':comms
    })