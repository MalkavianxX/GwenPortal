from django.shortcuts import render,redirect
from curso.models import Curso, Taller
from django.http import JsonResponse
from .models import Cupones,MiContenido ,ProgresoCurso, VideosVistos
import mercadopago
from django.conf import settings
#PAYPAL
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalhttp import HttpError
from paypalcheckoutsdk.core import PayPalHttpClient
from paypalcheckoutsdk.core.environment import LiveEnvironment

import requests
from  curso.models import Material,Curso,Taller
import json
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

class MicontenidoAux():
    def __init__(self, nombre, tipo, imagen, progreso,collection_id):
        self.nombre = nombre
        self.tipo = tipo
        self.imagen = imagen
        self.progreso = progreso
        self.collection_id = collection_id
class VideosAux():
        def __init__(self,nombre,tiempo,link,guid):
            self.nombre = nombre
            self.tiempo = tiempo
            self.link = link
            self.guid = guid
def format_seconds(seconds):
    hours = seconds // 3600  # Obtener las horas
    minutes = (seconds % 3600) // 60  # Obtener los minutos
    if hours >0:
    # Construir la cadena de formato
        formatted_time = f"{hours}h {minutes}m"
    else:
        formatted_time = f"{minutes}m"
    return formatted_time      

def marcar_completado(request, guid):
    complet = VideosVistos(
        video_guid=guid,
        usuario=request.user
    )
    complet.save()

    data = json.loads(request.body)
    id_library = data.get('id_library')
    id_collection = data.get('id_collection')
    data = {}

    return JsonResponse(data,status=200)

def iniciar_curso(request,id_library,id_collection):

    url = "https://video.bunnycdn.com/library/"+str(id_library)+"/videos?page=1&itemsPerPage=100&collection="+str(id_collection)+"&orderBy=date"
    acces_k = ""
    #curso
    if id_library == "132990":
        material = Material.objects.filter(curso = Curso.objects.get(id_collection = id_collection))

        acces_k = "6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd"
    #taller    
    elif id_library == "132992":
        material = Material.objects.filter(taller = Taller.objects.get(id_collection = id_collection))

        acces_k = "1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912"    

    headers = {
        "accept": "application/json",
        "AccessKey": acces_k
    }

    response = requests.get(url, headers=headers)
    response = response.json()
    videos = response["items"]
    lista_videos = []
    videos_visto = VideosVistos.objects.filter(usuario=request.user).values_list('video_guid', flat=True)
    lista_videos_vistos = []
    for video in videos:
        if video["guid"] not in videos_visto:
            lista_videos.append(
                VideosAux(
                video["title"],
                format_seconds(int(video["length"])),
                "https://iframe.mediadelivery.net/embed/"+str(video["videoLibraryId"])+"/"+str(video["guid"])+"?autoplay=false",
                video["guid"]
                )
            )
        else:
            lista_videos_vistos.append(
                VideosAux(
                video["title"],
                format_seconds(int(video["length"])),
                "https://iframe.mediadelivery.net/embed/"+str(video["videoLibraryId"])+"/"+str(video["guid"])+"?autoplay=false",
                video["guid"]
                )
            )
    if len(lista_videos) == 0:
        return render(request,'micontenido/iniciar_curso.html',{
            'videos':lista_videos[1:],
            'num_videos':response["totalItems"],
            'materiales':material,
            'id_library':id_library,
            'id_collection':id_collection,
            'videos_vistos':lista_videos_vistos,
            'cant_videos_vistos':len(lista_videos_vistos),
            'flag':1

        })
    else:
        return render(request,'micontenido/iniciar_curso.html',{
            'videos':lista_videos[1:],
            'num_videos':response["totalItems"],
            'materiales':material,
            'primer_video':lista_videos[0],
            'id_library':id_library,
            'id_collection':id_collection,
            'videos_vistos':lista_videos_vistos,


        })
@csrf_exempt
def cerrar_sesion(request):
    logout(request)
    return redirect('nombre_de_la_vista') 

# Create your views here.
def dash_micontenido(request):
    flag = True
    contenido = MiContenido.objects.filter(usuario = request.user).order_by('-fecha_inicio')
    lista_cursos = []
    lista_talleres = []
    for item in contenido: 
        if item.curso:
            lista_cursos.append(MicontenidoAux(
                item.curso.nombre,
                '132990',
                item.curso.imagen.url,
                ProgresoCurso.objects.get(inscripcion = item).porcentaje_completado,
                item.curso.id_collection
            ))
            print(item.curso.id_collection)    
        else:
            lista_talleres.append(MicontenidoAux(
                item.taller.nombre,
                '132992',
                item.taller.imagen.url,
                ProgresoCurso.objects.get(inscripcion = item).porcentaje_completado,
                item.taller.id_collection
            ))
            print(item.taller.id_collection)
           
    if (not lista_cursos and not lista_talleres):
        flag = False  
    return render(request,"micontenido/micontenido_dash.html",{
        'cursos':lista_cursos,
        'talleres': lista_talleres,
        'flag':flag
    })

#carrito

@csrf_exempt
def agregar_al_carrito(request, producto_id):
    try:
        producto = Taller.objects.get(id_collection = producto_id)
    except Taller.DoesNotExist:
        try:
            producto = Curso.objects.get(id_collection = producto_id)
        except Curso.DoesNotExist:
            response = {
                'status': 'error',
                'message': 'No se encontró el producto.'
            }
            return JsonResponse(response)

    if 'carrito' not in request.session:
        request.session['carrito'] = []

    carrito = request.session['carrito']
    carrito.append(producto_id)
    request.session['carrito'] = carrito

    response = {
        'status': 'success',
        'message': 'El producto se agregó al carrito exitosamente.',
        'producto': {
            'id': producto.id,
            'nombre': producto.nombre,
            'imagen':producto.imagen.url,
            'precio':producto.precio,
            'categoria':producto.categoria.nombre,
            'id_collection':producto.id_collection
            # Agrega otros campos del producto que desees incluir en la respuesta
        }
    }

    return JsonResponse(response)


def eliminar_del_carrito(request, producto_id):
    try:
        carrito = request.session.get('carrito', [])
        if producto_id in carrito:
            carrito.remove(producto_id)
            request.session['carrito'] = carrito
            response = {
                'status': 'success',
                'message': 'El producto se eliminó del carrito exitosamente.'
            }
        else:
            response = {
                'status': 'error',
                'message': 'El producto no existe en el carrito.'
            }
    except Exception as e:
        response = {
            'status': 'error',
            'message': 'Ocurrió un error al eliminar el producto del carrito.'
        }

    return JsonResponse(response)

class ProductoAux():
    def __init__(self, id, nombre, imagen, precio, categoria, id_collection):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.precio = precio
        self.categoria = categoria
        self.id_collection = id_collection
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'imagen': self.imagen,
            'precio': self.precio,
            'categoria': self.categoria,
            'id_collection': self.id_collection
        }

@csrf_exempt
def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    if 'descuento' not in request.session:
        request.session['descuento'] = 0
    desc = request.session['descuento']
   
    productos = []
    total = 0
    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
        
        producto_aux = ProductoAux(
            id=producto.id,
            nombre=producto.nombre,
            imagen=producto.imagen.url,
            precio=producto.precio,
            categoria=producto.categoria.nombre, 
            id_collection=producto.id_collection
        )
        total = total + float(producto.precio)
        productos.append(producto_aux.to_dict())

    response = {
        'carrito': carrito,
        'productos': productos,
        'total': str(total),
        'descuento': str(desc)
    }

    return JsonResponse(response)

def verificar_descuento(request, cupon):
    try:
        descuento = Cupones.objects.get(nombre=cupon)
        
        response = {
            'status': 'success',
            'message': f'Cupón de descuento de {descuento.valor}USD',
            'valor': descuento.valor
        }

        if 'descuento' not in request.session:
            request.session['descuento'] = 0
        desc = request.session['descuento']
        desc= descuento.valor
        request.session['descuento'] = desc

        return JsonResponse(response)
    except Cupones.DoesNotExist:
        response = {
            'status': 'error',
            'message': 'El cupón no existe'
        }
        return JsonResponse(response)
import mercadopago

def crear_preferencia_MP(request): 
    carrito = request.session.get('carrito', [])
    total = 0
    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
        total = total + float(producto.precio)

    sdk = mercadopago.SDK(settings.MERCADO_PAGO_CLIENT_SECRET)
    PUBLIC_KEY_MP=settings.MERCADO_PAGO_CLIENT_ID

    preference_data = {
        "items": [
            {
                "title": "Producto test",
                "quantity": 1,
                "currency_id": "USD", 
                "unit_price": str(total)
            }
        ],
        "back_urls": {
            "success": "https://gwenluy.com/micontenido/pago_success/",
            "failure": "https://gwenluy.com/micontenido/pago_danger/",
            "pending": "https://gwenluy.com/micontenido/pago_pendiente/"
        },
        "payer": {
            "name": "Juan",
            "surname": "Lopez",
            "email": "user@email.com",
        },
        "statement_descriptor": "Gwen Web",
        "binary_mode": True

    }

    preference = sdk.preference().create(preference_data)

    # Obtener el enlace de pago
    response_data = {
        'preference_id': preference["response"]["id"],
        'public_key_mp':PUBLIC_KEY_MP
    }
    return JsonResponse(response_data)

def crear_preferencia_PP(request):

    carrito = request.session.get('carrito', [])
    total = 0
    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
        total = total + float(producto.precio)

    environment = LiveEnvironment(client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
    client = PayPalHttpClient(environment)
    requestPaypal = OrdersCreateRequest()
    requestPaypal.prefer('return=representation')
    descuento = request.session.get('descuento')
    total = total - descuento
    if total > 0:
        requestPaypal.request_body (
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    { 
                        "amount": {
                            "currency_code": 'USD',
                            "value": str(total)
                        }
                    }
                ],
                "application_context":{
                    "return_url":"https://gwenluy.com/micontenido/pago_success/",
                    "cancel_url":"https://gwenluy.com/micontenido/pago_danger/",
                    "brand_name":"Gwen Cursos"
                }
            }
        )
        try:
            response = client.execute(requestPaypal)
            if response.result.status == 'CREATED':
                approval_url = str(response.result.links[1].href)
                print(approval_url)
                response_data = {
                    'link':approval_url
                
                }
                return JsonResponse(response_data)

        except IOError as ioe:
            if isinstance(ioe, HttpError):
                # Something went wrong server-side
                return render(request,'checkout/pago_cancelado.html')   
    else:
        pago_success(request)        

def pago_success(request):
    carrito = request.session.get('carrito', [])
    
    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
            nuevo_curso = MiContenido(
                usuario = request.user,
                curso = producto,

            )
            nuevo_curso.save()
            progeso = ProgresoCurso(
                inscripcion = nuevo_curso,
                porcentaje_completado = 0
            )
            progeso.save()
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
            nuevo_taller = MiContenido(
                usuario = request.user,
                taller = producto,

            )
            nuevo_taller.save()
            progeso = ProgresoCurso(
                inscripcion = nuevo_taller,
                porcentaje_completado = 0
            )
            progeso.save()
    request.session['carrito'] = []

    return render(request,"micontenido/pago_success.html")

def pago_danger(request):
    return render(request,"micontenido/pago_danger.html")

def pago_pendiente(request):
    return render(request,"micontenido/pago_pendiente.html")

def obtener_contenido(request):

    return JsonResponse()
@login_required(login_url='login_view')
def checkout(request):
    carrito = request.session.get('carrito', [])
    total = 0
    productos = []

    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
        
        producto_aux = ProductoAux(
            id=producto.id,
            nombre=producto.nombre,
            imagen=producto.imagen.url,
            precio=producto.precio,
            categoria=producto.categoria.nombre,
            id_collection=producto.id_collection
        )
        productos.append(producto_aux)

        total = total + float(producto.precio)

    carrito = request.session.get('carrito', [])
    total = 0
    for clave in carrito:
        try:
            producto = Curso.objects.get(id_collection=clave)
        except Curso.DoesNotExist:
            producto = Taller.objects.get(id_collection=clave)
        total = total + float(producto.precio)

    environment = LiveEnvironment(client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
    client = PayPalHttpClient(environment)
    requestPaypal = OrdersCreateRequest()
    requestPaypal.prefer('return=representation')
    if 'descuento' not in request.session:
        request.session['descuento'] = 0
    desc = request.session['descuento']
    f_total = total - float(desc)
    if f_total > 0:
        requestPaypal.request_body (
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {  
                        "amount": {
                            "currency_code": 'USD',
                            "value": str(f_total)
                        }
                    }
                ],
                "application_context":{
                    "return_url":"https://gwenluy.com/micontenido/pago_success/",
                    "cancel_url":"https://gwenluy.com/micontenido/pago_danger/",
                    "brand_name":"Gwen Cursos"
                }
            }
        )
        try:
            response = client.execute(requestPaypal)
            if response.result.status == 'CREATED':
                approval_url = str(response.result.links[1].href)

                return render(request,"micontenido/checkout.html",{
                    'cursos':productos,
                    'total':f_total,
                    'link': approval_url,
                    'descuento': float(desc),
                    'subtotal': float(total),
                })


        except IOError as ioe:
            if isinstance(ioe, HttpError):
                # Something went wrong server-side
                return render(request,'micontenido/pago_danger.html')           
        return render(request,"micontenido/checkout.html",{
            'cursos':productos,
            'total':total
        })
    else:
        for clave in carrito:
                try:
                    producto = Curso.objects.get(id_collection=clave)
                    nuevo_curso = MiContenido(
                        usuario = request.user,
                        curso = producto,

                    )
                    nuevo_curso.save()
                    progeso = ProgresoCurso(
                        inscripcion = nuevo_curso,
                        porcentaje_completado = 0
                    )
                    progeso.save()
                except Curso.DoesNotExist:
                    producto = Taller.objects.get(id_collection=clave)
                    nuevo_taller = MiContenido(
                        usuario = request.user,
                        taller = producto,

                    )
                    nuevo_taller.save()
                    progeso = ProgresoCurso(
                        inscripcion = nuevo_taller,
                        porcentaje_completado = 0
                    )
                    progeso.save()
        request.session['carrito'] = []

        return render(request,"micontenido/pago_success.html")
