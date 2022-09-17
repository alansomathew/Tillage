

from django.shortcuts import redirect, render
from Admin.models import Medicinecategory

from Guest.models import Newshop
from TillageWizards.models import  Complaintshop, Feedbackshop, NewMedicine
from User.models import Bookmedicine, Complaintusertoshop, Help
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def homepage(request):
    if 'shopid' in request.session:
        return render(request,'TillageWizards/Home.html')
    else:
        return redirect('Guest:Login')

def Myprofile(request):
    if 'shopid' in request.session:
        wizardobj=Newshop.objects.get(id=request.session["shopid"])
        return render(request,'TillageWizards/Myprofile.html',{"shop":wizardobj})
    else:
        return redirect('Guest:Login')

def editprofile(request):
    if 'shopid' in request.session:
        wizardobj=Newshop.objects.get(id=request.session["shopid"])
        if request.method=='POST' and request.FILES:
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            address=request.POST.get("address")
            logo=request.FILES.get("logo")
            wizardobj.name=name
            wizardobj.contact=contact
            wizardobj.address=address
            wizardobj.logo=logo
            wizardobj.save()
            return redirect('TillageWizards:my-profile')
        else:
            return render(request,'TillageWizards/Editprofile.html',{"shop":wizardobj})
    else:
        return redirect('Guest:Login')


def changepassword(request):
    if 'shopid' in request.session:
        wizardobj=Newshop.objects.get(id=request.session["shopid"])
        if request.method=='POST':
            passs=wizardobj.password
            cpass=request.POST.get("currentpassword")
            npass=request.POST.get("newpassword")
            if passs==cpass:
                wizardobj.password=npass
                wizardobj.save()
                return redirect('Guest:Login')
            else:
                pass
        else:
            return render(request,'TillageWizards/Changepassword.html')
    else:
        return redirect('Guest:Login')


def addproduct(request):
    if 'shopid' in request.session:
        pro=NewMedicine.objects.all()
        dis=Medicinecategory.objects.all()
        if request.method=='POST'and request.FILES:
            name=request.POST.get("productname")
            rate=request.POST.get("rate")
            details=request.POST.get("details")
            stock1=request.POST.get("stock")
            img=request.FILES.get("photo")
            cat=request.POST.get("medicinecategory")
            catobj=Medicinecategory.objects.get(id=cat)
            probj=Newshop.objects.get(id=request.session["shopid"])
            NewMedicine.objects.create(name=name,rate=rate,details=details,stock=stock1,shop=probj,photo=img,cat=catobj)
            return render(request,'TillageWizards/Newproduct.html',{"name":pro,"dis":dis})
        else:
            return render(request,'TillageWizards/Newproduct.html',{"name":pro,"dis":dis})
    else:
        return redirect('Guest:Login')


def delproduct(request,mid):
    if 'shopid' in request.session:
        pl=NewMedicine.objects.get(id=mid)
        pl.delete()
        return redirect("TillageWizards:Add-product")
    else:
        return redirect('Guest:Login')

def addstock(request,eid):
    if 'shopid' in request.session:
        pro=NewMedicine.objects.get(id=eid)
        if request.method=='POST':
            stock1=int(request.POST.get("stock"))
            oldstock=int(pro.stock)
            newstock=stock1+oldstock
            pro.stock=newstock
            pro.save()  
            return redirect("TillageWizards:Add-product") 
        else:
            return render(request,'TillageWizards/Addstock.html')
    else:
        return redirect('Guest:Login')


def viewbookmedicines(request):
    if 'shopid' in request.session:
        med=Bookmedicine.objects.filter(vstatus=0)
        return render(request,'TillageWizards/Orders.html',{"medicine":med})
    else:
        return redirect('Guest:Login')


def acceptmedicine(request,aid):
    if 'shopid' in request.session:
        medobj=Bookmedicine.objects.get(id=aid)
        email1=medobj.user.email
        name=medobj.user.name
        obj=medobj.medicine.id
        newobj=NewMedicine.objects.get(id=obj)
        stock1=int(newobj.stock)
        quan=int(medobj.quantity)
        bal=stock1-quan
        newobj.stock=bal
        medobj.vstatus='1'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\ryour booking is Successfully completed welcome to Tillage.\n Your delivery is expected in 7 workingdays.\n This is from Tillage team thank you for our booking service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        medobj.save()
        newobj.save()
        return redirect('/TillageWizards/Orders/')
    else:
        return redirect('Guest:Login')

def rejectmedicine(request,rid):
    if 'shopid' in request.session:
        medobj=Bookmedicine.objects.get(id=rid)
        email1=medobj.user.email
        name=medobj.user.name
        medobj.vstatus='2'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rsorry your booking process is Failed\nSorry to inform that you failed in the booking process .\n This is from Tillage team thank you for our booking service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        medobj.save()
        return redirect('/TillageWizards/Viewmedicine/')
    else:
        return redirect('Guest:Login')


def acceptorder(request):
    if 'shopid' in request.session:
        ac=Bookmedicine.objects.filter(vstatus=1)
        return render(request,'TillageWizards/Acceptedorder.html',{"medicine":ac})
    else:
        return redirect('Guest:Login')


def rejectorder(request):
    if 'shopid' in request.session:
        ac=Bookmedicine.objects.filter(vstatus=2)
        return render(request,'TillageWizards/Rejectedorder.html',{"medicine":ac})
    else:
        return redirect('Guest:Login')

def feedback(request):
    if 'shopid' in request.session:
        
        shopobj=Newshop.objects.get(id=request.session["shopid"])
        if request.method=='POST':
            feed=request.POST.get("feedback")
            Feedbackshop.objects.create(Feedback=feed,user=shopobj)
            return render(request,'/TillageWizards/Home/')
        else:
         return render(request,'TillageWizards/Feedbackshop.html')
    else:
        return redirect('Guest:Login')

def logout(request):
    del request.session['shopid']
    return redirect('Guest:Login')

def viewcompaint(request):
    if 'shopid' in request.session:
        com=Help.objects.all()
        return render(request,'TillageWizards/Viewcomplaints.html',{"complaints":com})
    else:
        return redirect('Guest:Login')

def accepthelp(request,aid):
    if 'shopid' in request.session:
        comobj=Help.objects.get(id=aid)
        email1=comobj.user.email
        name=comobj.user.name
        comobj.vstatus='1'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rWelcome our helpline service.\n Your complaint is verified and we will respond after fewhours.\n This is from Tillage team thank you for our helpline service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        comobj.save()
        return redirect('TillageWizards:View-complaints')
    else:
        return redirect('Guest:Login')


def rejecthelp(request,rid):
    if 'shopid' in request.session:
        comobj=Help.objects.get(id=rid)
        email1=comobj.user.email
        name=comobj.user.name
        comobj.vstatus='2'
        send_mail(
            'Respected sir/madam '+name, #subject
            "\rwelcome our helpline service\nyour complaint is verified your disease is not detected so we will respond after 7workingdays.\n This is from Tillage team thank you for our helpline service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Tillage.\n Thank you.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
        comobj.save()
        return redirect('TillageWizards:View-complaints')
    else:
        return redirect('Guest:Login')

def addconsulationfee(request,cid):
    if 'shopid' in request.session:
        pro=Help.objects.get(id=cid)
        if request.method=='POST':
            rate=int(request.POST.get("consultationfee"))
            pro.stock=rate
            pro.save()  
            return redirect('TillageWizards:View-complaints')
        else:
            return render(request,'TillageWizards/Consultationfee.html')
    else:
        return redirect('Guest:Login')

def complaintshop(request):
    if 'shopid' in request.session:
        shopobj=Newshop.objects.get(id=request.session["shopid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintshop.objects.create(content=con,attachment=att,shop=shopobj)
            return redirect('/TillageWizards/Home/')
        else:
            return render(request,'TillageWizards/complaintshop.html')
    else:
        return redirect('Guest:Login')

def viewcomplaintwizard(request):
    if 'shopid' in request.session:
        com=Complaintshop.objects.filter(shop=request.session["shopid"],vstatus=0)
        return render(request,'TillageWizards/Wizardscomplaintview.html',{"complaint":com})
    else:
        return redirect('Guest:Login')

def viewcomplaintusertoshop(request):
    if 'shopid' in request.session:
      com=Complaintusertoshop.objects.all()
      return render(request,'TillageWizards/Viewcomplaintusertoshop.html',{"complaint":com})
    else:
        return redirect('Guest:Login')
     

def replyusettoshop(request,usid):
    obj= Complaintusertoshop.objects.get(id=usid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('TillageWizards:viewuser-complaints')
    else:
        return render(request,'Admin/Reply.html')


def deliveringdate(request,bid):
    # if 'userid' in request.session:
        bobj=Bookmedicine.objects.get(id=bid)
        if request.method=='POST':
            dated=request.POST.get("date")
            bobj.delivering=dated
            bobj.dstatus='1'
            bobj.save()
            return redirect("TTillageWizards:View-Orders")
        else:

            return render(request,'TillageWizards/Date.html',{"viewdate":bobj})
    # else:
    #     return redirect('Guest:Login')
    