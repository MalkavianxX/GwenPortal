from django.shortcuts import render
from curso.models import Categoria, Curso, Taller
from inicio_sesion.models import Comentario
from blog.models import Post
# Create your views here.
def login(request):

    post = Post.objects.all().order_by('-fecha_publicacion')
    curso_cat = Categoria.objects.all().order_by('-nombre')[:4]
    header_1 = post[0]
    header_2 = post[1]
    header_3 = post[2]
    header_4 = post[3]
    print(header_4)
    for p in post: 
        p.fecha_publicacion = p.fecha_publicacion.strftime('%d-%m-%Y')    
    cursos = Curso.objects.all().order_by('-id')[:5]
    talleres = Taller.objects.all().order_by('-id')[:5]
    comms = Comentario.objects.filter(estatus = True).order_by('-fecha')
    return render(request,"login/login.html",{
        'cursos': cursos, 
        'talleres':talleres,
        'comms':comms,
        'posts':post,
        'cat_cursos':curso_cat,
        'header_1' : header_1,
        'header_2' : header_2,
        'header_3' : header_3,
        'header_4': header_4,
    })