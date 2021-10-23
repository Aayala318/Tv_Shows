from django.db import models
from django.http import request

# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        # postData == request.POST 
        if len(postData['title'])<2:
            errors['title'] ='Show title should be at least 2 characters.'
        if len(postData['network'])<3:
            errors['title'] ='Show network should be at least 3 characters.'
        # if len(postData['release_date']):
        #     errors['release_date'] ='Show title should be at least 2 characters.'
        if len(postData['description'])<10:
            errors['description'] ='Show description should be at least 10 characters.'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=25)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

