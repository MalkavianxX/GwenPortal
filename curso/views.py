from django.shortcuts import render, redirect
from .models import Categoria, Material, Curso, Video, Taller
from django.db.models import Count
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def dashboard_cursos(request):

    categorias = Categoria.objects.annotate(num_cursos=Count('curso')).order_by('-nombre')
    cursos = Curso.objects.annotate(num_videos=Count('video')).order_by('-fecha')
    cursos = cursos.annotate(cantidad_usuarios_cursando=Count('usuarios_cursando'))
    materiales = Material.objects.all().order_by('-tipo_archivo')
    return render(request,"curso/cursos.html",{
        'categorias':categorias,
        'cursos':cursos,
        'materiales':materiales
    }) 
def format_seconds(seconds):
    hours = seconds // 3600  # Obtener las horas
    minutes = (seconds % 3600) // 60  # Obtener los minutos
    if hours >0:
    # Construir la cadena de formato
        formatted_time = f"{hours}h {minutes}m"
    else:
        formatted_time = f"{minutes}m"
    return formatted_time

def ver_taller(request,id_taller):
    taller = Taller.objects.get(pk = id_taller)
    usuario = request.user

    class VideosAux():
        def __init__(self,nombre,tiempo) -> None:
            self.nombre = nombre
            self.tiempo = tiempo
    url = "https://video.bunnycdn.com/library/132992/videos?page=1&itemsPerPage=100&collection="+str(taller.id_collection)+"&orderBy=title"

    headers = {
        "accept": "application/json",
        "AccessKey": "1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912"
    }

    response = requests.get(url, headers=headers)

    response = response.json()
    videos = response["items"]
    total_time = 0
    lista_videos = []
    for video in videos:
        total_time = total_time + int(video["length"])
        lista_videos.append(
            VideosAux(video["title"],format_seconds(int(video["length"])))
        )
    total_time = format_seconds(total_time)     
    cant_videos = response["totalItems"]
    
    if usuario.is_staff:
        return render(request,"curso/ver_taller.html",{
            'taller':taller,
            'total_tiempo':total_time,
            'videos':lista_videos,
            'numvideos':cant_videos,
            'cant_material':Material.objects.filter(taller = taller).count(),
            'contenido_relacionado':Taller.objects.filter(categoria = taller.categoria)
        })    
    else:
        return render(request,"curso/public_ver_taller.html",{
            'taller':taller,
            'total_tiempo':total_time,
            'videos':lista_videos,
            'numvideos':cant_videos,
            'cant_material':Material.objects.filter(taller = taller).count(),
            'contenido_relacionado':Taller.objects.filter(categoria = taller.categoria)
        })   

def render_crear_curso(request):
    return render(request,"curso/crear_curso.html",{
        'categorias': Categoria.objects.all().order_by('-nombre')
    })
def render_crear_taller(request):
    return render(request,"curso/crear_taller.html",{
        'categorias': Categoria.objects.all().order_by('-nombre')
    })
def ver_curso(request,id_curso):
    usuario = request.user
    print(usuario.username)
    class VideosAux():
        def __init__(self,nombre,tiempo) -> None:
            self.nombre = nombre
            self.tiempo = tiempo
    curso = Curso.objects.get(pk = id_curso)
    url = "https://video.bunnycdn.com/library/132990/videos?page=1&itemsPerPage=100&collection="+str(curso.id_collection)+"&orderBy=title"

    headers = {
        "accept": "application/json",
        "AccessKey": "6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd"
    }

    response = requests.get(url, headers=headers)

    response = response.json()
    videos = response["items"]
    total_time = 0
    lista_videos = []
    for video in videos:
        total_time = total_time + int(video["length"])
        lista_videos.append(
            VideosAux(video["title"],format_seconds(int(video["length"])))
        )

    total_time = format_seconds(total_time)     
    cant_videos = response["totalItems"]
    if usuario.is_staff:
        return render(request,"curso/ver_curso.html",{
            'curso':curso,
            'total_tiempo':total_time,
            'videos':lista_videos,
            'numvideos':cant_videos,
            'cant_material':Material.objects.filter(curso = curso).count(),
            'contenido_relacionado':Curso.objects.filter(categoria = curso.categoria)
        })
    else:
        return render(request,"curso/public_ver_curso.html",{
            'curso':curso,
            'total_tiempo':total_time,
            'videos':lista_videos,
            'numvideos':cant_videos,
            'cant_material':Material.objects.filter(curso = curso).count(),
            'contenido_relacionado':Curso.objects.filter(categoria = curso.categoria)
        })


def dashboard_talleres(request):
    categorias = Categoria.objects.annotate(num_cursos=Count('taller')).order_by('-nombre')
    talleres = Taller.objects.annotate(num_videos=Count('video')).order_by('-fecha')
    talleres = talleres.annotate(cantidad_usuarios_cursando=Count('usuarios_cursando'))

    materiales = Material.objects.all().order_by('-tipo_archivo')
    return render(request,"curso/talleres.html",{
        'categorias':categorias,
        'talleres':talleres,
        'materiales':materiales
    })

@csrf_exempt
def guardar_curso(request):
    if request.method == 'POST':

        categoria = request.POST.get('categoria')
        nombre_curso = request.POST.get('nombre')
        descripcion = request.POST.get('descrip')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')  # Asegúrate de tener enctype="multipart/form-data" en tu formulario HTML


        url = "https://video.bunnycdn.com/library/132990/collections"

        payload = "{\"name\":\""+str(nombre_curso)+"\"}"
        headers = {
            "accept": "application/json",
            "content-type": "application/*+json",
            "AccessKey": "6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd"
        }

        response = requests.post(url, data=payload, headers=headers)
        guid = response.json()["guid"]
        curso = Curso(
            categoria = Categoria.objects.get(pk = categoria),
            nombre = nombre_curso,
            descripcion = descripcion,
            precio = float(precio),
            imagen = imagen,
            id_collection = guid
        )
        # Guardar el objeto Curso en la base de datos
        curso.save()
        # Enviar una respuesta al cliente
        return JsonResponse({'status': 'ok'})
    else:
        # Si la solicitud no es de tipo POST, enviar un error al cliente
        return JsonResponse({'status': 'error', 'message': 'El método de solicitud no es válido'})   
@csrf_exempt
def guardar_taller(request):
    if request.method == 'POST':

        categoria = request.POST.get('categoria')
        nombre_curso = request.POST.get('nombre')
        descripcion = request.POST.get('descrip')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')  # Asegúrate de tener enctype="multipart/form-data" en tu formulario HTML

        url = "https://video.bunnycdn.com/library/132992/collections"

        payload = "{\"name\":\""+str(nombre_curso)+"\"}"    
        headers = {
            "accept": "application/json",
            "content-type": "application/*+json",
            "AccessKey": "1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912"
        }

        response = requests.post(url, data=payload, headers=headers)

        guid = response.json()["guid"]
        curso = Taller(
            categoria = Categoria.objects.get(pk = categoria),
            nombre = nombre_curso,
            descripcion = descripcion,
            precio = float(precio),
            imagen = imagen,
            id_collection = guid
        )
        # Guardar el objeto Curso en la base de datos
        curso.save()
        # Enviar una respuesta al cliente
        return JsonResponse({'status': 'ok'})
    else:
        # Si la solicitud no es de tipo POST, enviar un error al cliente
        return JsonResponse({'status': 'error', 'message': 'El método de solicitud no es válido'})   

def public_todos_cursos(request):
    cursos = Curso.objects.all().order_by('-categoria')
    return render(request,"curso/public_todos_cursos.html",{
        'cursos':cursos,
    })

def public_todos_talleres(request):
    talleres = Taller.objects.all().order_by('-categoria')
    return render(request,"curso/public_todos_talleres.html",{
       
        'talleres':talleres
    })

def public_todos_gratis(request):
    cursos = Curso.objects.filter(precio  = 0.0).order_by('-categoria')
    talleres = Taller.objects.filter(precio  = 0.0).order_by('-categoria')    
    return render(request,"curso/public_todos_gratis.html",{
        'cursos':cursos,
        'talleres':talleres
    })    