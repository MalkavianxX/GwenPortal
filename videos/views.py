from django.shortcuts import render
from curso.models import Curso,Categoria,Taller
import requests

# Create your views here.
def dashboard_videos(request):
    return render(request,"videos/videos_dash.html",{
        'cursos':Curso.objects.all().order_by('-fecha'),
        'talleres':Taller.objects.all().order_by('-fecha')
    }) 
def mostar_todos_videos(request,id_librari):
    class Manager_video():
        def __init__(self,curso,nombre_video,peso,link):
            self.curso = curso
            self.nombre_video = nombre_video

            self.peso = peso
            self.link = link
    if id_librari == "132990":
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
        total_videos = lista_videos["totalItems"]
        lista_videos = lista_videos["items"]
        for video_iter in lista_videos:
            
            for curso in lista_cursos:


                if curso["guid"] == video_iter["collectionId"]:
                    video_iter["collectionId"] = curso["name"]

            videos.append( Manager_video(
                curso = video_iter["collectionId"],
                nombre_video = video_iter["title"],
                peso = "{0:.2f}MB".format(int( video_iter["storageSize"]) / 1048576),
                link = "https://iframe.mediadelivery.net/embed/132990/"+str(video_iter["guid"])+"?autoplay=false"
            ))
        titulo = "Cursos"
    elif id_librari == "132992":
        #obtener todos los cursos
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
        total_videos = lista_videos["totalItems"]
        lista_videos = lista_videos["items"]
        for video_iter in lista_videos:
            
            for curso in lista_cursos:


                if curso["guid"] == video_iter["collectionId"]:
                    video_iter["collectionId"] = curso["name"]

            videos.append( Manager_video(
                curso = video_iter["collectionId"],
                nombre_video = video_iter["title"],
                peso = "{0:.2f}MB".format(int( video_iter["storageSize"]) / 1048576),
                link = "https://iframe.mediadelivery.net/embed/132992/"+str(video_iter["guid"])+"?autoplay=false"
            ))
        titulo = "Talleres"
           

    return render(request,"videos/todos_videos.html",{"videos":videos,"num_videos":total_videos,"titulo":titulo})