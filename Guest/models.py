from django.db import models
from Admin.models import District,Place

# Create your models here.
class Newuser(models.Model):
      name=models.CharField(max_length=50)
      contact=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      address=models.TextField(max_length=50)
      password=models.CharField(max_length=50)
      place=models.ForeignKey(Place,on_delete=models.CASCADE)
      doj=models.DateField(auto_now_add=True,null=True)
      vstatus=models.IntegerField(default=False,null=True)


class Newshop(models.Model):
      name=models.CharField(max_length=50)
      contact=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      address=models.TextField(max_length=50)
      password=models.CharField(max_length=50)
      place=models.ForeignKey(Place,on_delete=models.CASCADE)
      ownername=models.CharField(max_length=50,null=True)
      ownercontact=models.CharField(max_length=50,null=True)
      owneremail=models.EmailField(max_length=15,unique=True,null=True)
      logo=models.FileField(upload_to='uploads/shopimages/',null=True)
      proof=models.FileField(upload_to='uploads/shopproof/',null=True)
      doj=models.DateField(auto_now_add=True,null=True)
      vstatus=models.IntegerField(default=False,null=True)

class Newdeigner(models.Model):
      name=models.CharField(max_length=50)
      contact=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      address=models.TextField(max_length=50)
      password=models.CharField(max_length=50)
      place=models.ForeignKey(Place,on_delete=models.CASCADE)
      logo=models.FileField(upload_to='uploads/shopdesigner/')
      proof=models.FileField(upload_to='uploads/designerproof/')
      doj=models.DateField(auto_now_add=True)
      vstatus=models.IntegerField(default=False)
      wstatus=models.IntegerField(default=False)