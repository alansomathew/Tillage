from django.db import models
from Admin.models import Medicinecategory

from Guest.models import Newshop, Newuser

# Create your models here.
class NewMedicine(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    details=models.CharField(max_length=80)
    stock=models.IntegerField()
    photo=models.ImageField(upload_to='uploads/medicineimages/')
    doj=models.DateField(auto_now_add=True)
    shop=models.ForeignKey(Newshop,on_delete=models.CASCADE)
    cat=models.ForeignKey(Medicinecategory,on_delete=models.CASCADE,null=True)
    

class Feedbackshop(models.Model):
    doc=models.DateField(auto_now_add=True)
    wizards=models.ForeignKey(Newshop,on_delete=models.CASCADE)
    Feedback=models.TextField(max_length=50)

class Complaintshop(models.Model):
    content=models.TextField(max_length=100)
    shop=models.ForeignKey(Newshop,on_delete=models.CASCADE,null=True)
    attachment=models.FileField(upload_to='uploads/complaintshopimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)