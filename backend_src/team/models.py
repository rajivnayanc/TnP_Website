from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_page/')
    batch = models.IntegerField()
    position = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    year = models.IntegerField()

    
    def __str__(self):
        return self.name