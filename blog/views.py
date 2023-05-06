from django.shortcuts import render,redirect
from .models import Post,CategoriaPost
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def nada(request):
    return render(request,"blog/nada.html",{
        'categorias':CategoriaPost.objects.all().order_by('-nombre')
    })

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('categoria-blog-nombre')
        descripcion = request.POST.get('categoria-blog-descripcion')
        nueva_categoria = CategoriaPost(nombre=nombre, descripcion=descripcion)
        nueva_categoria.save()
    categorias = list(CategoriaPost.objects.values())
    return JsonResponse({'categorias': categorias})

def get_categorias(request):
    categorias = list(CategoriaPost.objects.values())
    return JsonResponse({'categorias': categorias})    


@csrf_exempt
def publicar_post(request):
    if request.method == 'POST':
        # Obtener los datos enviados desde el cliente
        titulo = request.POST.get('titulo', '')
        categoria_id = request.POST.get('categoria', '')
        contenido = request.POST.get('contenido', '')
        archivo = request.FILES.get('archivo', None)
        estilo_color_fondo = request.POST.get('estilo_color_fondo', '')
        estilo_color_letra = request.POST.get('estilo_color_letra', '')
        estilo_fuente_letra = request.POST.get('estilo_fuente_letra', '')
        estilo_tamano_letra_titulo = request.POST.get('estilo_tamano_letra_titulo', '')
        estilo_tamano_letra_cuerpo = request.POST.get('estilo_tamano_letra_cuerpo', '')

        # Crear una instancia del modelo Post y guardarla en la base de datos
    
        post = Post(
            titulo=titulo,
            categoria=CategoriaPost.objects.get(nombre = categoria_id),
            contenido=contenido,
            autor='Gewndolyn',
            estilo_color_fondo=estilo_color_fondo,
            estilo_color_letra=estilo_color_letra,
            estilo_fuente_letra=estilo_fuente_letra,
            estilo_tamano_letra_titulo=estilo_tamano_letra_titulo,
            estilo_tamano_letra_cuerpo=estilo_tamano_letra_cuerpo
        )
        if archivo:
            post.archivo = archivo
        post.save()

        # Enviar una respuesta al cliente
        return JsonResponse({'status': 'ok'})
    else:
        # Si la solicitud no es de tipo POST, enviar un error al cliente
        return JsonResponse({'status': 'error', 'message': 'El método de solicitud no es válido'})
