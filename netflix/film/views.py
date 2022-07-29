import profile
from django.shortcuts import render,redirect
from film.models import Film 
import random
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(request,name):
     return render(request,"film/hello.html",{'name_param': name})


########################################favorit#########################################################
@login_required
def add_favorite_film(request,film_id):
    le_film = Film.objects.filter(id = film_id).first()
    user = request.user

    if le_film in user.profile.films.all():
        messages.warning(request,"le film {} est deja dans votre favoris".format(le_film.title))
    else:
        user.profile.films.add(le_film)
        user.profile.save()
        messages.success(request,"le film {} a bien été ajouter dans votre favoris".format(le_film.title))
    return redirect('film-home')

@login_required
def mylist_film(request):
    films = Film.objects.filter(profile=request.user.profile)
    films = list(films)

    taille_mylist = len(films)

    return render(request,"film/mylist_film.html",{'films':films,'taille_mylist':taille_mylist})
 
@login_required
def remove_favorite_film(request,film_id):
    le_film = Film.objects.filter(id = film_id).first()

    user = request.user
    user.profile.films.remove(le_film)
    user.profile.save()
        
    messages.success(request,"le film {} a bien été supprimé des votre favoris".format(le_film.title))
    return redirect('film-home') 
#################################################################################################

########################################like#########################################################
@login_required
def liker(request,film_id):
    le_film = Film.objects.filter(id = film_id).first()
    user = request.user

    if user in le_film.likeur.all():
        messages.warning(request,"vous avais deja like le nom du film {}".format(le_film.title))
    else:
        le_film.likeur.add(user)
        le_film.save()
        messages.success(request,"vous avais bien like le film suivent {}".format(le_film.title))
    return redirect('film-home')

#################################################################################################


#################################################CRUD sur film#############################################

def home(request):
    films = Film.objects.all()
    films = list(films)
    
    random.shuffle(films)
    films_aleatoire = random.choices(films,k=4)

    likes = {}
    for film in films:
        likes[film] = len(film.likeur.all())


    return render(request,"film/home.html",{"likes":likes,"films_aleatoire" : films_aleatoire })
  

# def filmDetail(request,pk):
#       film =Film.objects.filter(id=pk).first()
#       return render(request,"film/film_detail.html",{'object':film})

class FilmDetail(DetailView):
      model = Film
class FilmCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Film
    fields = ['title','description','image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FilmUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Film
    fields = ['title','description','image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
class FilmDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Film
    success_url= "/"

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False






    

