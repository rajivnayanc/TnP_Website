from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Recruiter
def index(request):
    recruiters = Recruiter.objects.all()
    context = {
        'recruiters':recruiters
    }
    return render(request,'recruiters/index.html',context=context)
