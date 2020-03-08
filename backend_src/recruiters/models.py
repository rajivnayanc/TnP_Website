from django.db import models

# Create your models here.

class Recruiter(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField(upload_to='recruiters/', max_length=100)

    def __str__(self):
        return self.name