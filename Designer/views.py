from django.shortcuts import redirect, render
from Designer.models import  Complaintdesigner, Feedbackdesigner, Services

from Guest.models import Newdeigner
from User.models import Complaintusertodesigner

# Create your views here.
def homepage(request):
    if 'desiid' in request.session:
        return render(request,'Designer/Home.html')
    else:
        return redirect('Guest:Login')

def Myprofile(request):
    if 'desiid' in request.session:
        desiobj=Newdeigner.objects.get(id=request.session["desiid"])
        return render(request,'Designer/Myprofile.html',{"designer":desiobj})
    else:
        return redirect('Guest:Login')

def editprofile(request):
    if 'desiid' in request.session:
        desiobj=Newdeigner.objects.get(id=request.session["desiid"])
        if request.method=='POST' and request.FILES:
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            address=request.POST.get("address")
            logo=request.FILES.get("logo")
            desiobj.name=name
            desiobj.contact=contact
            desiobj.address=address
            desiobj.logo=logo
            desiobj.save()
            return redirect('Designer:my-profile')
        else:
            return render(request,'Designer/Editprofile.html',{"designer":desiobj})
    else:
        return redirect('Guest:Login')


def changepassword(request):
    if 'desiid' in request.session:
        desiobj=Newdeigner.objects.get(id=request.session["desiid"])
        if request.method=='POST':
            passs=desiobj.password
            cpass=request.POST.get("currentpassword")
            npass=request.POST.get("newpassword")
            if passs==cpass:
                desiobj.password=npass
                desiobj.save()
                return redirect('Guest:Login')
            else:
                pass
        else:
            return render(request,'Designer/Changepassword.html')
    else:
        return redirect('Guest:Login')


def services(request):
    if 'desiid' in request.session:
        pro=Services.objects.all()
        if request.method=='POST'and request.FILES:
            name=request.POST.get("modelname")
            rate=request.POST.get("rate")
            details=request.POST.get("details")
            img=request.FILES.get("photo")
            probj=Newdeigner.objects.get(id=request.session["desiid"])
            Services.objects.create(name=name,rate=rate,details=details,design=probj,logo=img)
            return render(request,'Designer/Newservices.html',{"name":pro})
        else:
            return render(request,'Designer/Newservices.html',{"name":pro})
    else:
        return redirect('Guest:Login')

def delservice(request,mid):
    if 'desiid' in request.session:
        pl=Services.objects.get(id=mid)
        pl.delete()
        return redirect("Designer:Add-Services")
    else:
        return redirect('Guest:Login')

def feedback(request):
    if 'desiid' in request.session:
        designerobj=Newdeigner.objects.get(id=request.session["desiid"])
        if request.method=='POST':
            feed=request.POST.get("feedback")
            Feedbackdesigner.objects.create(Feedback=feed,user=designerobj)
            return render(request,'Designer/Home/')
        else:
            return render(request,'Designer/Feedbackdesigner.html')
    else:
        return redirect('Guest:Login')

def complaintdesigner(request):
    if 'desiid' in request.session:
        designerobj=Newdeigner.objects.get(id=request.session["desiid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintdesigner.objects.create(content=con,attachment=att,designer=designerobj)
            return redirect('/Designer/Home/')
        else:
            return render(request,'Designer/complaintdesigner.html')
    else:
        return redirect('Guest:Login')

def logout(request):
    del request.session['desiid']
    return redirect('Guest:Login')

def viewcomplaintdesigner(request):
    if 'desiid' in request.session:
        com=Complaintdesigner.objects.filter( designer=request.session["desiid"],vstatus=0)
        return render(request,'Designer/Designercomplaintview.html',{"complaint":com})
    else:
        return redirect('Guest:Login')
        
def viewcomplaintuserdesigner(request):
    if 'desiid' in request.session:
      designerobj=Complaintusertodesigner.objects.all()
      return render(request,'Designer/Viewusercomplaint.html',{"designer":designerobj}) 
    else:
        return redirect('Guest:Login')
    

def replyusertodesigner(request,rdid):
    obj= Complaintusertodesigner.objects.get(id=rdid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('Designer:Complaint Designer')
    else:
        return render(request,'Designer/Replydesigner.html')