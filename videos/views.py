from django.shortcuts import render
from curso.models import Curso,Categoria,Taller, Material
import requests
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class Manager_video():
    def __init__(self,curso,nombre_video,peso,link,tipo):
        self.curso = curso
        self.nombre_video = nombre_video

        self.peso = peso
        self.link = link
        self.tipo = tipo
# Create your views here.

def dashboard_videos(request):

    return render(request,"videos/videos_dash.html",{
        'cursos':Curso.objects.all().order_by('-fecha'),
        'talleres':Taller.objects.all().order_by('-fecha')
    }) 
def mostrar_vtalleres(request):
    obj = obtener_vtalleres_full()
    return render(request,"videos/mostrar_vtalleres.html",{
        'videos':obj,
        'total':len(obj),
        'titulo':"Talleres"

    })
def mostrar_vcursos(request):
    obj = obtener_vcursos_full()
    return render(request,"videos/mostrar_vtalleres.html",{
        'videos':obj,
        'total':len(obj),
        'titulo':"Cursos"

    })    

def render_subir_video(request):
    print("CANTIDAD DE VIDEOS --------------------------------")

    cursos = Curso.objects.annotate(cantidad_usuarios_cursando=Count('usuarios_cursando'))
    talleres = Taller.objects.annotate(cantidad_usuarios_cursando=Count('usuarios_cursando')) 
     
    for i in cursos:
        i.descripcion = "https://dash.bunny.net/stream/132990/library/video?collection="+str(i.id_collection)
    for i in talleres:
        i.descripcion = "https://dash.bunny.net/stream/132992/library/video?collection="+str(i.id_collection)


    return render(request,"videos/subir_video.html",{
        "cursos":cursos,
        "talleres":talleres
    })

def obtener_vcursos_full():
    #obtener todos los cursos
    url = "https://video.bunnycdn.com/library/132990/collections?page=1&itemsPerPage=100&orderBy=date"

    headers = {
        "accept": "application/json",
        "AccessKey": "6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd"
    }
    response = requests.get(url, headers=headers)
    lista_cursos = response.json()
    lista_cursos = lista_cursos["items"]
    videos = []
    
    #obtener todos los videos
    url = "https://video.bunnycdn.com/library/132990/videos?page=1&itemsPerPage=100&orderBy=collectionId"

    headers = {
        "accept": "application/json",
        "AccessKey": "6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd"
    }
    response_videos = requests.get(url, headers=headers)
    lista_videos = response_videos.json() 
    lista_videos = lista_videos["items"]
    for video_iter in lista_videos:
        
        for curso in lista_cursos:


            if curso["guid"] == video_iter["collectionId"]:
                video_iter["collectionId"] = curso["name"]

        videos.append( Manager_video(
            curso = ["collectionId"] ,
            nombre_video = video_iter["title"],
            peso = "{0:.2f}MB".format(int( video_iter["storageSize"]) / 1048576),
            link = "https://iframe.mediadelivery.net/embed/132990/"+str(video_iter["guid"])+"?autoplay=false",
            tipo = "curso"
        ))
    return videos
    
def obtener_vtalleres_full():
    url = "https://video.bunnycdn.com/library/132992/collections?page=1&itemsPerPage=100&orderBy=date"

    headers = {
        "accept": "application/json",
        "AccessKey": "1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912"
    }
    response = requests.get(url, headers=headers)
    lista_cursos = response.json()
    lista_cursos = lista_cursos["items"]
    videos = []
    
    #obtener todos los videos
    url = "https://video.bunnycdn.com/library/132992/videos?page=1&itemsPerPage=100&orderBy=collectionId"

    headers = {
        "accept": "application/json",
        "AccessKey": "1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912"
    }
    response_videos = requests.get(url, headers=headers)
    lista_videos = response_videos.json() 
    lista_videos = lista_videos["items"]
    for video_iter in lista_videos:
        
        for curso in lista_cursos:


            if curso["guid"] == video_iter["collectionId"]:
                video_iter["collectionId"] = curso["name"]

        videos.append( Manager_video(
            curso = video_iter["collectionId"] ,
            nombre_video = video_iter["title"],
            peso = "{0:.2f}MB".format(int( video_iter["storageSize"]) / 1048576),
            link = "https://iframe.mediadelivery.net/embed/132992/"+str(video_iter["guid"])+"?autoplay=false",
            tipo = "taller"
        ))
    return videos

def mostar_todos_videos(request):
    vcursos = obtener_vcursos_full()
    vtalleres = obtener_vtalleres_full()
    vtalleres.extend(vcursos)
    for i in vtalleres:
        print(i.curso, i.nombre_video, i.peso,i.link, i.tipo)

    return render(request,"videos/todos_videos.html",{
        'videos':vtalleres,
        'total':len(vtalleres),
    })

def render_archivos_dash(request):
    material = Material.objects.all()
    cursos = Curso.objects.all()
    talleres = Taller.objects.all()
    return render(request,"videos/arch_dash.html",{
        'talleres':talleres,
        'cursos':cursos,
        'materiales':material
    })

@csrf_exempt  # Solo para simplificar en este ejemplo, asegúrate de manejar CSRF adecuadamente en producción
def guardar_archivo_curso(request):
    if request.method == 'POST':
        curso_id = request.POST.get('curso_id')
        nombre_archivo = request.POST.get('nombre_archivo')
        tipo_archivo = request.POST.get('tipo_archivo')
        archivo = request.FILES.get('archivo')

        nuevo_archivo = Material(
            curso=Curso.objects.get(pk =curso_id ),
            nombre_archivo=nombre_archivo,
            tipo_archivo=tipo_archivo, 
            archivo=archivo
        )
        nuevo_archivo.save()

        response_data = {'mensaje': 'Archivo guardado exitosamente'}
        return JsonResponse(response_data,status = 200)
    else:
        response_data = {'error': 'Método no permitido'}
        return JsonResponse(response_data, status=405)
    
@csrf_exempt  # Solo para simplificar en este ejemplo, asegúrate de manejar CSRF adecuadamente en producción
def guardar_archivo_taller(request):
    if request.method == 'POST':
        taller_id = request.POST.get('taller_id')
        nombre_archivo = request.POST.get('nombre_archivo')
        tipo_archivo = request.POST.get('tipo_archivo')
        archivo = request.FILES.get('archivo')

        nuevo_archivo = Material(
            taller=Taller.objects.get(pk =taller_id ),
            nombre_archivo=nombre_archivo,
            tipo_archivo=tipo_archivo, 
            archivo=archivo
        )
        nuevo_archivo.save()

        response_data = {'mensaje': 'Archivo guardado exitosamente'}
        return JsonResponse(response_data,status = 200)
    else:
        response_data = {'error': 'Método no permitido'}
        return JsonResponse(response_data, status=405)