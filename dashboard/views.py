from django.core.checks import messages
from django.shortcuts import render
from . forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def notes(request):
    form = NotesForm()
    context = {'form':form}
    return render(request,'dashboard/notes.html',context)
   


      