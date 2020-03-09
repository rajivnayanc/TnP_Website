from django.shortcuts import render
from .models import Introduction,IAM,Speakers,Projects, Tracks, Projects, Participants
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

def tracklist(request,id):
    event = IAM.objects.get(pk=id)
    tracks = Tracks.objects.filter(iam=event).all()
    context = {
        'event_id':event.id,
        'tracks':tracks
    }
    return render(request,'IAM/tracks.html',context)

def projectlist(request,id,track_id):
    # event = IAM.objects.get(pk=id)
    track = Tracks.objects.get(pk=track_id)
    projects = Projects.objects.filter(track=track).all()
    context = {
        'event_id':id,
        'track_id':track_id,
        'track_name':track.track,
        'projects':projects
    }
    return render(request,'IAM/projectlist.html',context)

def projectDetail(request,id,track_id,project_id):
    project = Projects.objects.get(pk=project_id)
    context = {
        'project':project
    }
    return render(request,'IAM/projectDetail.html',context)