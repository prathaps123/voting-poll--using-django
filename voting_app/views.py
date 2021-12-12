from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    d=Data.objects.all()
    return render(request,'home.html',{'d':d})

def new(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('adhar_id') and request.POST.get('voter_id') and request.POST.get('vote'):
            data=Data()
            data.name=request.POST.get('name')
            data.adhar_id=request.POST.get('adhar_id')
            data.voter_id=request.POST.get('voter_id')
            data.vote=request.POST.get('vote')
            data.save()
            return redirect('/')
    return render(request,'new.html')
   
            
