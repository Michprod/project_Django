from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'{} votre comte a ete cree avec succes'.format(username))
            return redirect('login')
    else :
        form = UserCreationForm()
    return render(request,"users/register.html",{"form_register" : form})
