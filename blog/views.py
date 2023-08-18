from django.shortcuts import render,redirect
from .models import Post,CategoriaPost
from curso.models import Categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def nada(request):
    post = Post.objects.all().order_by('-fecha_publicacion')
    for p in post:
        p.fecha_publicacion = p.fecha_publicacion.strftime('%d-%m-%Y')
    return render(request,"blog/nada.html",{
        'categorias':CategoriaPost.objects.all().order_by('-nombre'),
        'posts':post
    })

def render_escribir(request):
    return render(request,"blog/escribir.html",{
        'categorias':CategoriaPost.objects.all().order_by('-nombre'),

    })
def render_categorias(request):
    return render(request,"blog/categorias.html",{
        'cats':CategoriaPost.objects.all().order_by('-nombre'),
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
 

        # Crear una instancia del modelo Post y guardarla en la base de datos
    
        post = Post( 
            titulo=titulo,
            categoria=CategoriaPost.objects.get(id = categoria_id),
            contenido=contenido,
            autor='Gewndolyn',
       
        )
        if archivo:
            post.imagen = archivo
        post.save()

        # Enviar una respuesta al cliente
        return JsonResponse({'status': 'ok'})
    else:
        # Si la solicitud no es de tipo POST, enviar un error al cliente
        return JsonResponse({'status': 'error', 'message': 'El método de solicitud no es válido'})

def ver_post(request,id_post):
    post = Post.objects.get(pk = id_post)
    relative_post = Post.objects.filter(categoria = post.categoria).order_by('-fecha_publicacion')
    return render(request,"blog/vista_blog.html",{
        'post':post,
        'otros_post':relative_post
    })

def mostrar_blog(request):
    post = Post.objects.all().order_by('-fecha_publicacion')
    curso_cat = Categoria.objects.all().order_by('-nombre')[:4]
    header_1 = post[0]
    header_2 = post[1]
    header_3 = post[2]
    header_4 = post[3]
    print(header_4)
    for p in post: 
        p.fecha_publicacion = p.fecha_publicacion.strftime('%d-%m-%Y')
    return render(request,"blog/todos_posts.html",{
        'posts':post,
        'cat_cursos':curso_cat,
        'header_1' : header_1,
        'header_2' : header_2,
        'header_3' : header_3,
        'header_4': header_4,
    })