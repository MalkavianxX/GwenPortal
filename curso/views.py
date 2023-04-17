from django.shortcuts import render

# Create your views here.
def nada(request):
    return render(request,"curso/cursos.html")