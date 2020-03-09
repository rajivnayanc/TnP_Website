from django.shortcuts import render
from .models import Branch, Category, Subject
# Create your views here.

def index(request):
    branches = Branch.objects.all()
    subjects = {}
    for i in branches:
        subjects[i] = [i.description,[]]
        temp = Subject.objects.filter(branch=i)
        # print(temp,type(temp))
        subjects[i][1] += temp
    print(branches)
    # print('------------')
    print(subjects)
    context = {
        'branch':branches,
        'subject':subjects
    }
    return render(request,'courses/courses.html',context)