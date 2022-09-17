
from django.db import models

from Guest.models import Newdeigner, Newuser

# Create your models here.

class Services(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    details=models.CharField(max_length=80)
    logo=models.FileField(upload_to='uploads/serviceimages/')
    design=models.ForeignKey(Newdeigner,on_delete=models.CASCADE)
    
    

class Feedbackdesigner(models.Model):
    doc=models.DateField(auto_now_add=True)
    designer=models.ForeignKey(Newdeigner,on_delete=models.CASCADE)
    Feedback=models.TextField(max_length=50)

class Complaintdesigner(models.Model):
    content=models.TextField(max_length=100)
    designer=models.ForeignKey(Newdeigner,on_delete=models.CASCADE,null=True)
    attachment=models.FileField(upload_to='uploads/complaintimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)