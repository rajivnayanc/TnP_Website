from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Introduction)
admin.site.register(models.IAM)
admin.site.register(models.Speakers)
admin.site.register(models.Tracks)
admin.site.register(models.Projects)
admin.site.register(models.Participants)
admin.site.register(models.Winners)
