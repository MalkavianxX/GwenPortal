from django.shortcuts import render
from inicio_sesion.models import Comentario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def dashboard_comentarios(request):

    return render(request,"comentarios/dash_comentarios.html",{
        'comentarios':Comentario.objects.all().order_by('-fecha')
    })

@csrf_exempt
def guardar_comentario(request):    
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))

        comentario = data.get("comentario")
        # Haz lo que necesites con el comentario, como guardarlo en el modelo
        # ...
        if comentario:
            usuario = request.user 
            
            comentario = Comentario.objects.create(usuario=usuario, comentario=comentario)
            comentario.save()
        
        else:
            return JsonResponse(data={'mensaje': 'comentario vacio'}, status=400)


        # Enviar una respuesta JSON exitosa o con error según corresponda
        return JsonResponse(data={'mensaje': 'Creacion exitosa'}, status=200)   
    else:
        return JsonResponse(data={'mensaje': 'comentario vacio'}, status=400)

def aprobar_comm(request):
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))

        comm_id = data.get("comm_id")
        # Haz lo que necesites con el comentario, como guardarlo en el modelo
        # ...
        comm = Comentario.objects.get(pk = comm_id)
        comm.estatus = True
        comm.save()

        # Enviar una respuesta JSON exitosa o con error según corresponda
        return JsonResponse(data={'mensaje': 'Creacion exitosa'}, status=200)   
    else:
        return JsonResponse(data={'mensaje': 'error'}, status=400)
    
def denegar_comm(request):
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))

        comm_id = data.get("comm_id")
        # Haz lo que necesites con el comentario, como guardarlo en el modelo
        # ...
        comm = Comentario.objects.get(pk = comm_id)
        comm.estatus = False
        comm.save()

        # Enviar una respuesta JSON exitosa o con error según corresponda
        return JsonResponse(data={'mensaje': 'Creacion exitosa'}, status=200)   
    else:
        return JsonResponse(data={'mensaje': 'error'}, status=400)
def eliminar_comm(request):
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))

        comm_id = data.get("comm_id")
        # Haz lo que necesites con el comentario, como guardarlo en el modelo
        # ...
        comm = Comentario.objects.get(pk = comm_id)
        comm.delete()
        # Enviar una respuesta JSON exitosa o con error según corresponda
        return JsonResponse(data={'mensaje': 'Creacion exitosa'}, status=200)   
    else:
        return JsonResponse(data={'mensaje': 'error'}, status=400)    