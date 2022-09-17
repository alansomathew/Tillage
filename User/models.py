

from django.db import models
from Admin.models import Category, Wizards

from Guest.models import Newdeigner, Newshop, Newuser
from TillageWizards.models import NewMedicine

# Create your models here.

class Newproduct(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    stock=models.IntegerField()
    photo=models.ImageField(upload_to='uploads/productimages/')
    doj=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

class Bookproduct(models.Model):
    bod=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE)
    product=models.ForeignKey(Newproduct,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    shipment=models.CharField(max_length=50)
    totalprice=models.FloatField()
    vstatus=models.IntegerField(default=False)
    pstatus=models.IntegerField(default=False)
    delivering=models.CharField(max_length=50,null=True,default="Processing")
    dstatus=models.IntegerField(default=False)

class Bookmedicine(models.Model):
    doj=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE)
    medicine=models.ForeignKey(NewMedicine,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    shipment=models.CharField(max_length=50,null=True)
    totalprice=models.IntegerField()
    vstatus=models.IntegerField(default=False)
    pstatus=models.IntegerField(default=False)
    delivering=models.CharField(max_length=50,null=True,default="Processing")
    dstatus=models.IntegerField(default=False)


class Feedbackuser(models.Model):
    doc=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE)
    Feedback=models.TextField(max_length=50)

class Help(models.Model):
    doc=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='uploads/diseaseimages/')
    discription=models.TextField(max_length=50)
    title=models.TextField(max_length=15)
    vstatus=models.IntegerField(default=False)
    consulationfee=models.IntegerField(default=False)
    wizard= models.ForeignKey(Wizards,on_delete=models.CASCADE,null=True)


class Complaintuser(models.Model):
    content=models.TextField(max_length=100)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE,null=True)
    attachment=models.FileField(upload_to='uploads/complaintuserimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)

class Complaintusertoshop(models.Model):
    content=models.TextField(max_length=100)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE,null=True)
    attachment=models.FileField(upload_to='uploads/complaintusertoshopimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)

class Complaintusertodesigner(models.Model):
    content=models.TextField(max_length=100)
    user=models.ForeignKey(Newuser,on_delete=models.CASCADE,null=True)
    designer=models.ForeignKey(Newdeigner,on_delete=models.CASCADE,null=True)
    attachment=models.FileField(upload_to='uploads/complaintusertodesignerimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)

class Complaintproduct(models.Model):
    content=models.TextField(max_length=100)
    fromuser=models.ForeignKey(Newuser,on_delete=models.CASCADE,null=True,related_name="fromuser")
    touser=models.ForeignKey(Newuser,on_delete=models.CASCADE,null=True,related_name="touser")
    attachment=models.FileField(upload_to='uploads/complaintproductimages/')
    vstatus=models.IntegerField(default=False)
    replay=models.TextField(max_length=100,default="noreply")
    doc=models.DateField(auto_now_add=True)


class chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        Newuser, on_delete=models.SET_NULL,default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey (
        Newuser ,on_delete=models.SET_NULL,default=False, null=True, related_name="to_user")
    from_wizards = models.ForeignKey(
        Wizards, on_delete=models.SET_NULL,default=False, null=True, related_name="from_wizards")
    to_wizards = models.ForeignKey (
        Wizards, on_delete=models.SET_NULL,default=False, null=True, related_name="to_wizards")
    content = models.TextField()

    
    
