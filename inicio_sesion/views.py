from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def login_view(request):

    return render(request,"inicio_sesion/login.html")

def log_out(request):
    logout(request)

    return redirect('login')
@csrf_exempt
# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(data={'mensaje': 'Inicio de sesión exitoso'}, status=200)
        else:
            return JsonResponse(data={'mensaje': 'Nombre de usuario o contraseña incorrecta'}, status=400)
    else:
        return JsonResponse(data={'mensaje': 'Método no permitido'}, status=405)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrsena')
        email = request.POST.get('email')
        first_name = request.POST.get('nombre')
        # Validar que el usuario no exista
        if User.objects.filter(username=username).exists():
            return JsonResponse(data={'mensaje': 'Usuario ya existe'}, status=400)
        else:
                
            # Crear el usuario
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.save()
            # Iniciar sesión
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return JsonResponse(data={'mensaje': 'Creacion exitoso'}, status=200)
    else:
        return JsonResponse(data={'mensaje': 'Método no permitido'}, status=405)

def render_dashboard(request):
    return render(request,"inicio_sesion/dashboard.html")


def render_seccion_inicio_dashboard(request):
    return render(request, "inicio_sesion/dashboard/inicio.html")

def render_seccion_blog_dashboard(request):
    return redirect('nada-blog')

def render_seccion_cursos_dashboard(request):
    return render(request, "inicio_sesion/dashboard/cursos.html")

def render_seccion_talleres_dashboard(request):
    return render(request, "inicio_sesion/dashboard/talleres.html")

def render_seccion_biblioteca_dashboard(request):
    return render(request, "inicio_sesion/dashboard/biblioteca.html")

def render_seccion_usuarios_dashboard(request):
    return render(request, "inicio_sesion/dashboard/usuarios.html")

def render_seccion_mensajes_dashboard(request):
    return render(request, "inicio_sesion/dashboard/mensajes.html")

def render_seccion_estadisticas_dashboard(request):
    return render(request, "inicio_sesion/dashboard/estadisticas.html")

