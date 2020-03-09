from django.db import models

# Create your models here.
class Introduction(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class IAM(models.Model):
    event_name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.FileField(upload_to='iam/logo', max_length=100,blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    winner_declared = models.BooleanField()
    def __str__(self):
        return self.event_name

class Speakers(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='iam/speakers', max_length=100)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    description = models.TextField()
    iam = models.ForeignKey("IAM.IAM", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name,self.iam.event_name)

class Tracks(models.Model):
    track = models.CharField(max_length=255)
    iam = models.ForeignKey("IAM.IAM", on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.track,self.iam.event_name)

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    track = models.ForeignKey("IAM.Tracks", on_delete=models.CASCADE,related_name='project_track')
    iam = models.ForeignKey("IAM.IAM", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name,self.iam.event_name)
    

class Participants(models.Model):
    name = models.CharField(max_length=255)
    iam = models.ForeignKey("IAM.IAM", on_delete=models.CASCADE)
    project = models.ForeignKey("IAM.Projects", on_delete=models.CASCADE,related_name='project_participants')

    def __str__(self):
        return "{} - {}".format(self.name,self.iam.event_name)
    
class Winners(models.Model):
    project = models.ForeignKey("IAM.Projects", on_delete=models.CASCADE,related_name='winners_project')
    iam = models.ForeignKey("IAM.IAM", on_delete=models.CASCADE)
    rank = models.IntegerField()

    def __str__(self):
        return "{}".format(self.project)
    