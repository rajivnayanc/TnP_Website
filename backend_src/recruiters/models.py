from django.db import models

# Create your models here.

class CompanyType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Recruiter(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField(upload_to='recruiters/', max_length=100)
    type = models.ForeignKey("recruiters.CompanyType",blank=True,null=True, on_delete=models.CASCADE,related_name='company_with_type')
    def __str__(self):
        return self.name