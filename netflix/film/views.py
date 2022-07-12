from django.shortcuts import render
from film.models import Film 
import random
# Create your views here.

def hello(request,name):
     return render(request,"film/hello.html",{'name_param': name})

def home(request):
    films = Film.objects.all()
    films = list(films)
    
    random.shuffle(films)
    films_aleatoire = random.choices(films,k=4)

    return render(request,"film/home.html",{"films":films,"films_aleatoire" : films_aleatoire })
  

def filmDetail(request,pk):
      film =Film.objects.filter(id=pk).first()
      return render(request,"film/film_detail.html",{'object':film})