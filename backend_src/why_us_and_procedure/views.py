from django.shortcuts import render
from .models import Why_Us, Procedure
# Create your views here.

def why_us(request):
    objects = Why_Us.objects.all()[0]
    context = {
        'objects':objects
    }
    return render(request,'why_us/index.html',context=context)

def procedure(request):
    objects = Procedure.objects.all()
    context = {
        'objects':objects
    }
    return render(request,'procedure/index.html',context)
