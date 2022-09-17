
from django.db import models


# Create your models here.
class District(models.Model):
    district=models.CharField(max_length=50)

class Place(models.Model):
    place=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

class Category(models.Model):
    category=models.CharField(max_length=50)

class Medicinecategory(models.Model):
    medicinecategory=models.CharField(max_length=50)

class Adminlogin(models.Model):
    adminemail=models.EmailField(max_length=50,unique=True)
    adminpassword=models.CharField(max_length=50)
   

class Wizards(models.Model):
      name=models.TextField(max_length=50)
      contact=models.CharField(max_length=10)
      email=models.EmailField(max_length=50,unique=True)
      details=models.CharField(max_length=50,null=True)
      license=models.FileField(upload_to='uploads/wizardlicense/')
      Logo=models.FileField(upload_to='uploads/wizardlogo/')
      password=models.CharField(max_length=50)