from django.db import models

# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + self.branch.title

class Subject(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' | ' + self.category.title

