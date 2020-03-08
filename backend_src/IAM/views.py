from django.shortcuts import render
from .models import Introduction,IAM,Speakers,Projects
# Create your views here.
def index(request):
    introduction = Introduction.objects.all()[0]
    events = IAM.objects.all().order_by('-date')
    context = {
        'introduction':introduction,
        'iam_events':events
    }
    return render(request,'IAM/index.html',context)

def detail(request,id):
    event = IAM.objects.get(pk=id)
    speakers = Speakers.objects.filter(iam=event).all()
    projects = Projects.objects.filter(iam=event).all()
    # print(len(speakers),len(projects))
    context = {
        'event':event,
        'speaker_len':len(speakers),
        'projects_len':len(projects),
        'winner_declared':event.winner_declared
    }
    return render(request,'IAM/detail.html',context)

def speakerlist(request,id):
    event = IAM.objects.get(pk=id)
    speakers = Speakers.objects.filter(iam=event).all()
    context = {
        'event_id':event.id,
        'speakers':speakers
    }
    return render(request,'IAM/speakerslist.html',context)

def speakerDetail(request,id,speaker_id):
    speaker = Speakers.objects.get(pk=speaker_id)
    print(speaker.name)
    context = {
        'speaker':speaker
    }
    return render(request,'IAM/speakerDetail.html',context)