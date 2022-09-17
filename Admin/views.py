from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from Admin.models import Adminlogin, Category, District, Medicinecategory,  Place, Wizards
from Designer.models import Complaintdesigner, Feedbackdesigner

from Guest.models import Newdeigner, Newshop, Newuser
from TillageWizards.models import Complaintshop, Feedbackshop
from User.models import Complaintuser, Feedbackuser
from User.views import complaintuser


def homepage(request):
    if 'adminid' in request.session:
        return render(request,'Admin/Home.html')
    else:
        return redirect('Guest:Login')

def Myprofile(request):
    # if 'desiid' in request.session:
        adminobj=Adminlogin.objects.get(id=request.session["adminid"])
        return render(request,'Admin/Myprofile.html',{"admin":adminobj})
    # else:
    #     return redirect('Guest:Login')

    
def dis(request):
    if 'adminid' in request.session:
        dis=District.objects.all()
        if request.method=='POST':
            name=request.POST.get("district")
            District.objects.create(district=name)
            return render(request,'Admin/District.html',{"name":dis})
        else:
            return render(request,'Admin/District.html',{"name":dis})
    else:
        return redirect('Guest:Login')


def deldis(request,disid):
    if 'adminid' in request.session:
        dis=District.objects.get(id=disid)
        dis.delete()
        return redirect("Admin:District")
    else:
        return redirect('Guest:Login')

def editdis(request,eid):
    if 'adminid' in request.session:
        dis=District.objects.get(id=eid)
        if request.method=='POST':
            name=request.POST.get("district")
            dis.district=name
            dis.save()
            return redirect("Admin:District")
        else:
            return render(request,'Admin/District.html',{"dname":dis})
    else:
        return redirect('Guest:Login')

def pl(request):
    if 'adminid' in request.session:
        pl=Place.objects.all()
        dis=District.objects.all()
        if request.method=='POST':
            name=request.POST.get("place")
            dist=request.POST.get("District")
            disobj=District.objects.get(id=dist)
            pin=request.POST.get("pincode")
            Place.objects.create(place=name,district=disobj,pincode=pin)
            return render(request,'Admin/Place.html',{"name":pl,"dis":dis})
        else:
            return render(request,'Admin/Place.html',{"name":pl,"dis":dis})
    else:
        return redirect('Guest:Login')

def delpl(request,pid):
    if 'adminid' in request.session:
        pl=Place.objects.get(id=pid)
        pl.delete()
        return redirect("Admin:Place")
    else:
        return redirect('Guest:Login')


def cat(request):
    if 'adminid' in request.session:
        cat=Category.objects.all()
        if request.method=='POST':
            name=request.POST.get("category")
            Category.objects.create(category=name)
            return render(request,'Admin/Category.html',{"name":cat})
        else:
            return render(request,'Admin/Category.html',{"name":cat})
    else:
        return redirect('Guest:Login')


def delcat(request,cid):
    if 'adminid' in request.session:
        cat=Category.objects.get(id=cid)
        cat.delete()
        return redirect("Admin:Category")
    else:
        return redirect('Guest:Login')


def editcat(request,cid):
    if 'adminid' in request.session:
        cat=Category.objects.get(id=cid)
        catall=Category.objects.all()
        if request.method=='POST':
            name=request.POST.get("category")
            cat.category=name
            cat.save()
            return redirect("Admin:Category")
        else:
            return render(request,'Admin/Category.html',{"cname":cat,"name":catall})
    else:
        return redirect('Guest:Login')

def viewuser(request):
    if 'adminid' in request.session:
        userobj=Newuser.objects.filter(vstatus=0)
        return render(request,'Admin/Newuser.html',{"user":userobj})
    else:
        return redirect('Guest:Login')


def viewrejectuser(request):
    if 'adminid' in request.session:
        userobj=Newuser.objects.filter(vstatus=2)
        return render(request,'Admin/Rejecteduser.html',{"user":userobj})
    else:
        return redirect('Guest:Login')


def acceptuser(request,aid):
    if 'adminid' in request.session:
        userobj=Newuser.objects.get(id=aid)
        email1=userobj.email
        name=userobj.name
        passwo=userobj.password
        userobj.vstatus='1'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Successfully welcome to Tillage.\n Your Password is" + passwo + " \nand your Username  is " + email1 + ".\n This is from Tillage team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        userobj.save()
        return redirect('/Admin/User/')
    else:
        return redirect('Guest:Login')

def rejectuser(request,rid):
    if 'adminid' in request.session:
        userobj=Newuser.objects.get(id=rid)
        email1=userobj.email
        name=userobj.name
        userobj.vstatus='2'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Failed.welcome to Tillage.\nSorry to inform that you failed in the verification process .\n This is from Tillage team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        userobj.save()
        return redirect('/Admin/User/')
    else:
        return redirect('Guest:Login')

def viewshop(request):
    if 'adminid' in request.session:
        sh=Newshop.objects.filter(vstatus=0)
        return render(request,'Admin/Newshop.html',{"shop":sh})
    else:
        return redirect('Guest:Login')

def viewrejectshop(request):
    if 'adminid' in request.session:
        shopobj=Newshop.objects.filter(vstatus=2)
        return render(request,'Admin/Rejectedshop.html',{"shop":shopobj})
    else:
        return redirect('Guest:Login')



def acceptshop(request,aid):
    if 'adminid' in request.session:
        shopobj=Newshop.objects.get(id=aid)
        email1=shopobj.email
        name=shopobj.name
        passwo=shopobj.password
        shopobj.vstatus='1'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Successfully welcome to Tillage.\n Your Password is" + passwo + " and your Username  is " + email1 + ".\n This is from Tillage team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        shopobj.save()
        return redirect('/Admin/Shop/')
    else:
        return redirect('Guest:Login')


def rejectshop(request,rid):
    if 'adminid' in request.session:
        shopobj=Newshop.objects.get(id=rid)
        email1=shopobj.email
        name=shopobj.name
        shopobj.vstatus='2'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Failed.welcome to Tillage.\nSorry to inform that you failed in the verification process .\n This is from Tillage team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        shopobj.save()
        return redirect('/Admin/Shop/')
    else:
        return redirect('Guest:Login')


def viewdesigner(request):
    if 'adminid' in request.session:
        desi=Newdeigner.objects.filter(vstatus=0)
        return render(request,'Admin/Newdesigner.html',{"designer":desi})
    else:
        return redirect('Guest:Login')


def viewrejectdesigner(request):
    if 'adminid' in request.session:
        designerobj=Newdeigner.objects.filter(vstatus=2)
        return render(request,'Admin/Rejecteddesigner.html',{"designer":designerobj})
    else:
        return redirect('Guest:Login')


def acceptdesigner(request,aid):
    if 'adminid' in request.session:
        desiobj=Newdeigner.objects.get(id=aid)
        email1=desiobj.email
        name=desiobj.name
        passwo=desiobj.password
        desiobj.vstatus='1'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Successfully welcome to Tillage.\n Your Password is" + passwo + " and your Username  is " + email1 + ".\n This is from Tillage team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        desiobj.save()
        return redirect('/Admin/Designer/')
    else:
        return redirect('Guest:Login')

def rejectdesigner(request,rid):
    if 'adminid' in request.session:
        desiobj=Newdeigner.objects.get(id=rid)
        email1=desiobj.email
        name=desiobj.name
        desiobj.vstatus='2'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Failed.welcome to Tillage.\nSorry to inform that you failed in the verification process .\n This is from Tillage team thank you for signing up to our service.\r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        desiobj.save()
        return redirect('/Admin/Designer/')
    else:
        return redirect('Guest:Login')

def accshop(request):
    if 'adminid' in request.session:
        acshop=Newshop.objects.filter(vstatus=1)
        return render(request,'Admin/Acceptedshop.html',{"shop":acshop})
    else:
        return redirect('Guest:Login')

def accuser(request):
    if 'adminid' in request.session:
        acuser=Newuser.objects.filter(vstatus=1)
        return render(request,'Admin/Accepteduser.html',{"user":acuser})
    else:
        return redirect('Guest:Login')

def accdesigner(request):
    if 'adminid' in request.session:
        acdesigner=Newdeigner.objects.filter(vstatus=1)
        return render(request,'Admin/Accepteddesigner.html',{"designer":acdesigner})
    else:
        return redirect('Guest:Login')



def medicinecat(request):
    if 'adminid' in request.session:
        cat=Medicinecategory.objects.all()
        if request.method=='POST':
            name=request.POST.get("medicinecategory")
            Medicinecategory.objects.create(medicinecategory=name)
            return render(request,'Admin/Medicinecategory.html',{"mname":cat})
        else:
            return render(request,'Admin/Medicinecategory.html',{"mname":cat})
    else:
        return redirect('Guest:Login')


def delmedicinecat(request,mcid):
    if 'adminid' in request.session:
        cat=Medicinecategory.objects.get(id=mcid)
        cat.delete()
        return redirect("Admin:Medicinecategory")
    else:
        return redirect('Guest:Login')

def editmedicinecat(request,meid):
    if 'adminid' in request.session:
        cat=Medicinecategory.objects.get(id=meid)
        catall=Medicinecategory.objects.all()
        if request.method=='POST':
            name=request.POST.get("medicinecategory")
            cat.medicinecategory=name
            cat.save()
            return redirect("Admin:Medicinecategory")
        else:
            return render(request,'Admin/Medicinecategory.html',{"cname":cat,"name":catall})
    else:
        return redirect('Guest:Login')

def viewfeedbackuser(request):
    if 'adminid' in request.session:
        userobj=Feedbackuser.objects.all()
        return render(request,'Admin/Viewuserfeedback.html',{"user":userobj})
    else:
        return redirect('Guest:Login')


def viewfeedbackshop(request):
    if 'adminid' in request.session:
        shopobj=Feedbackshop.objects.all()
        return render(request,'Admin/viewshopfeedback.html',{"shop":shopobj})
    else:
        return redirect('Guest:Login')

def viewfeedbackdesigner(request):
    if 'adminid' in request.session:
        designerobj=Feedbackdesigner.objects.all()
        return render(request,'Admin/Viewdesignerfeedback.html',{"designer":designerobj})
    else:
        return redirect('Guest:Login')   

def viewcomplaintuser(request):
    if 'adminid' in request.session:
        userobj=Complaintuser.objects.all()
        return render(request,'Admin/Viewusercomplaint.html',{"user":userobj})
    else:
        return redirect('Guest:Login')   

def viewcomplaintshop(request):
    if 'adminid' in request.session:
        wizardobj=Complaintshop.objects.all()
        return render(request,'Admin/viewshopcomplaint.html',{"wizard":wizardobj})
    else:
        return redirect('Guest:Login')   
 

def viewcomplaintdesigner(request):
    if 'adminid' in request.session:
        designerobj=Complaintdesigner.objects.all()
        return render(request,'Admin/Viewdesignercomplaint.html',{"designer":designerobj})    
    else:
        return redirect('Guest:Login')   

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        return redirect('Guest:Login')
    else:
        return redirect('Guest:Login')   


def replyuser(request,cid):
    obj=Complaintuser.objects.get(id=cid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('Admin:Usercomplaint')
    else:
        return render(request,'Admin/Reply.html')

def replyshop(request,rsid):
    obj= Complaintshop.objects.get(id=rsid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        print(rep)
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('Admin:Wizardscomplaint')
    else:
        return render(request,'Admin/Reply.html')

def replydesigner(request,rdid):
    obj= Complaintdesigner.objects.get(id=rdid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('Admin:Designercomplaint')
    else:
        return render(request,'Admin/Reply.html')

def replywizards(request,rdid):
    obj= Wizards.objects.get(id=rdid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('Admin:Wizardcomplaint')
    else:
        return render(request,'Admin/Reply.html')


def wizards(request):
        pro=Wizards.objects.all()
        if request.method=='POST'and request.FILES:
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            email=request.POST.get("email")
            details=request.POST.get("details")
            license=request.FILES.get("license")
            img=request.FILES.get("logo")
            password=request.POST.get("password")
            Wizards.objects.create(name=name,contact=contact,details=details,Logo=img,email=email,license=license,password=password)
            return render(request,'Admin/Wizards.html',{"wizard":pro})
        else:
            return render(request,'Admin/Wizards.html',{"wizard":pro})

  






        
