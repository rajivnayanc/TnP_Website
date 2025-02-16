from django.shortcuts import render
from .models import Team
from django.db.models import Q
# Create your views here.
def index(request, year):
    po = Team.objects.filter(position='Placement Officer',batch=year)
    if po:
        po = po[0]
    else:
        po = None
    teams = Team.objects.filter(Q(batch=year) & ~Q(position='Placement Officer')).order_by('-batch')
    years = Team.objects.values('batch').distinct().order_by('batch')
    context = {
        'years':{
            'years':years,
            'previous':year-1,
            'next': year+1,
        },
        'teams':teams,
        'po':po
    }
    return render(request,'team_page/index.html',context)