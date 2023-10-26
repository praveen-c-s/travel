# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import People

def demo(request):
     obj=Place.objects.all()
     oii=People.objects.all()
     return render(request,"index.html",{'result':obj,'final':oii})


# def addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      return render(request,"result.html",{'result':res})

