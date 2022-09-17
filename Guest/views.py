
from django.shortcuts import redirect, render

from Admin.models import Adminlogin, District, Place, Wizards
from Guest.models import Newdeigner, Newshop, Newuser
from User.models import Newproduct



# Create your views here.


def newuser(request):
    dis=District.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        email1=request.POST.get("email")
        Address=request.POST.get("address")
        plac=request.POST.get("Place")
        placeobj=Place.objects.get(id=plac)
        password=request.POST.get("password")
        
        Newuser.objects.create(name=name,contact=contact,email=email1,address=Address,place=placeobj,password=password)
        return render(request,'Guest/Newuser.html',{"dis":dis})
    else:
        return render(request,'Guest/Newuser.html',{"dis":dis}) 

def loadplace(request):
    dis=request.GET.get("disid")
    placeobj=Place.objects.filter(district=dis)
    return render(request,'Guest/loadplace.html',{"name":placeobj})

def newshop(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        address=request.POST.get("address")
        plac=request.POST.get("Place")
        placeobj=Place.objects.get(id=plac)
        password=request.POST.get("password")
        logo=request.FILES.get("logo")
        proof=request.FILES.get("proof")
        ownername=request.POST.get("ownername")
        ownercontact=request.POST.get("ownercontact")
        owneremail=request.POST.get("owneremail")
        Newshop.objects.create(name=name,contact=contact,email=email,address=address,place=placeobj,password=password,logo=logo,proof=proof,ownername=ownername,ownercontact=ownercontact,owneremail=owneremail)
        return render(request,'Guest/Newshop.html',{"dis":dis})
    else:
        return render(request,'Guest/Newshop.html',{"dis":dis}) 

def newdesigner(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        address=request.POST.get("address")
        plac=request.POST.get("Place")
        placeobj=Place.objects.get(id=plac)
        password=request.POST.get("password")
        logo=request.FILES.get("logo")
        proof=request.FILES.get("proof")
        Newdeigner.objects.create(name=name,contact=contact,email=email,address=address,place=placeobj,password=password,logo=logo,proof=proof)
        return render(request,'Guest/Newdesigner.html',{"dis":dis})
    else:
        return render(request,'Guest/Newdesigner.html',{"dis":dis}) 

def login(request):

    if request.method=="POST":
        em=request.POST.get("email")
        pa=request.POST.get("password")
        usercount=Newuser.objects.filter(email=em,password=pa,vstatus='1').count()
        shopcount=Newshop.objects.filter(email=em,password=pa,vstatus='1').count()
        designercount=Newdeigner.objects.filter(email=em,password=pa,vstatus='1').count()
        admincount=Adminlogin.objects.filter(adminemail=em,adminpassword=pa).count()
        wizardcount=Wizards.objects.filter(email=em,password=pa).count()




        if usercount>0:
            userobj=Newuser.objects.get(email=em,password=pa,vstatus='1')
            request.session["userid"]=userobj.id
            return redirect('User:User-Home')

        elif shopcount>0:
            wizardsobj=Newshop.objects.get(email=em,password=pa,vstatus='1')
            request.session["shopid"]=wizardsobj.id
            return redirect('TillageWizards:wizards-home')
        
        elif designercount>0:
            desiobj=Newdeigner.objects.get(email=em,password=pa,vstatus='1')
            print(desiobj)
            request.session["desiid"]=desiobj.id
            return redirect('Designer:Designer-Home')
        
        elif admincount>0:
            adminobj=Adminlogin.objects.get(adminemail=em,adminpassword=pa)
            request.session["adminid"]=adminobj.id
            return redirect('Admin:Home')
        
        elif wizardcount>0:
            wizardsobj=Wizards.objects.get(email=em,password=pa)
            request.session["wizardid"]=wizardsobj.id
            return redirect('Wizards:WizardsHome')

    else:
        return render(request,'Guest/Login.html')

def viewhome(request):
    probj=Newproduct.objects.all()
    return render(request,'Guest/Home.html',{"obj":probj})


       
        
    

