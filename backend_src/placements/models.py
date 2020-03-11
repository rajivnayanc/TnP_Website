from django.db import models
from django.utils.text import slugify
# Create your models here.

class Batch(models.Model):
    batch_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.batch_name)
        super(Batch,self).save(*args,**kwargs)

    def __str__(self):
        return self.batch_name


class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    def __str__(self):
        return self.branch_name

class JobDescription(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type
    
class Students(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey("placements.Branch",  on_delete=models.CASCADE,related_name='student_chosen_branch')
    batch = models.ForeignKey("placements.Batch", on_delete=models.CASCADE,related_name='student_of_batch')
    salary = models.FloatField()
    company = models.ForeignKey("recruiters.Recruiter", on_delete=models.CASCADE,related_name='student_company_name')
    Job_description = models.ForeignKey("placements.JobDescription", on_delete=models.CASCADE,related_name='student_job_roles')

    def __str__(self):
        return "{} | {}".format(self.name,self.batch)
    