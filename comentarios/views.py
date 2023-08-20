from django.shortcuts import render

# Create your views here.
def dashboard_comentarios(request):
    return render(request,"comentarios/dash_comentarios.html")