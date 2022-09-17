
from turtle import title
from django.shortcuts import redirect, render
from Admin.models import Category, Medicinecategory, Wizards
from Designer.models import Services
from django.conf import settings
from django.core.mail import send_mail
from Guest.models import Newdeigner, Newshop, Newuser
from TillageWizards.models import  Complaintshop, NewMedicine
from User.models import Bookmedicine, Bookproduct, Complaintproduct, Complaintuser, Complaintusertodesigner, Complaintusertoshop, Feedbackuser, Help, Newproduct, chat

# Create your views here.


def homepage(request):
    if 'userid' in request.session:
        return render(request,'User/Home.html')
    else:
        return redirect('Guest:Login')

def Myprofile(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        return render(request,'User/Myprofile.html',{"user":userobj})
    else:
        return redirect('Guest:Login')


def editprofile(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            address=request.POST.get("address")
            userobj.name=name
            userobj.contact=contact
            userobj.address=address
            userobj.save()
            return redirect('User:my-profile')
        else:
            return render(request,'User/Editprofile.html',{"user":userobj})
    else:
        return redirect('Guest:Login')


def changepassword(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            passs=userobj.password
            cpass=request.POST.get("currentpassword")
            npass=request.POST.get("newpassword")
            if passs==cpass:
                userobj.password=npass
                userobj.save()
                return redirect('Guest:Login')
            else:
                pass
        else:
            return render(request,'User/Changepassword.html')
    else:
        return redirect('Guest:Login')

        
def product(request):
    if 'userid' in request.session:
        dis=Category.objects.all()
        pro=Newproduct.objects.all()
        if request.method=='POST'and request.FILES:
            name=request.POST.get("productname")
            rate=request.POST.get("rate")
            
            stock1=request.POST.get("stock")
            img=request.FILES.get("photo")
            probj=Newuser.objects.get(id=request.session["userid"])
            Newproduct.objects.create(name=name,rate=rate,stock=stock1,user=probj,photo=img)
            return render(request,'User/Newproduct.html',{"name":pro,"dis":dis})
        else:
            return render(request,'User/Newproduct.html',{"name":pro,"dis":dis})
    else:
        return redirect('Guest:Login')

def delproduct(request,pid):
    if 'userid' in request.session:
        pl=Newproduct.objects.get(id=pid)
        pl.delete()
        return redirect("User:Add-product")
    else:
        return redirect('Guest:Login')

def addstock(request,eid):
    if 'userid' in request.session:
        pro=Newproduct.objects.get(id=eid)
        if request.method=='POST':
            stock1=int(request.POST.get("stock"))
            oldstock=int(pro.stock)
            newstock=stock1+oldstock
            pro.stock=newstock
            pro.save()  
            return redirect("User:Add-product") 
        else:
            return render(request,'User/Addstock.html')
    else:
        return redirect('Guest:Login')

def searchproduct(request):
    if 'userid' in request.session:
        dis=Category.objects.all()
        userobj=Newuser.objects.get(id=request.session["userid"])
        pro=Newproduct.objects.all()
        if request.method=='POST':
            category1=request.POST.get("category")
            print(category1)
            catobj=Category.objects.get(id=category1)
            pro=Newproduct.objects.filter(cat=catobj)
            print(pro)
            return render(request,'User/Searchproduct.html',{"name":pro,"dis":dis})
        else:
            return render(request,'User/Searchproduct.html',{"name":pro,"dis":dis})
    else:
        return redirect('Guest:Login')

def searchmedicine(request):
    if 'userid' in request.session:
        med=Medicinecategory.objects.all()
        print(med)
        pro=NewMedicine.objects.all()
        if request.method=='POST':
            category1=request.POST.get("medicinecategory")
            print(category1)
            catobj=Medicinecategory.objects.get(id=category1)
            pro=NewMedicine.objects.filter(cat=catobj)
            print(pro)
            return render(request,'User/Searchmedicine.html',{"name":pro,"med":med})
        else:
            return render(request,'User/Searchmedicine.html',{"name":pro,"med":med})
    else:
        return redirect('Guest:Login')

def searchservice(request):
    if 'userid' in request.session:
        mo=Services.objects.all()
        print(mo)
        return render(request,'User/Searchservices.html',{"name":mo})
    else:
        return redirect('Guest:Login')


def viewmoreservice(request,sid):
    if 'userid' in request.session:
        mo=Services.objects.get(id=sid)
        return render(request,'User/Viewmoreservices.html',{"name":mo})
    else:
        return redirect('Guest:Login')


def viewmoreproduct(request,pid):
    if 'userid' in request.session:
        mo=Newproduct.objects.get(id=pid)
        return render(request,'User/Viewmoreproduct.html',{"name":mo})
    else:
        return redirect('Guest:Login')

def viewmoremedicine(request,mid):
    if 'userid' in request.session:
        mo=NewMedicine.objects.get(id=mid)
        return render(request,'User/Viewmoremedicine.html',{"name":mo})
    else:
        return redirect('Guest:Login')

def buyproduct(request,bpid):
    if 'userid' in request.session:
        mo=Newproduct.objects.get(id=bpid)
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            quan=request.POST.get("quantity")
            ship=request.POST.get("shippingcharge")
            topr=request.POST.get("totalprice")
            Bookproduct.objects.create(quantity=quan,totalprice=topr,user=userobj,product=mo,shipment=ship)
            return render(request,'User/Buyproduct.html',{"name":mo,"user":userobj})
        else:
            return render(request,'User/Buyproduct.html',{"name":mo,"user":userobj})
    else:
        return redirect('Guest:Login')
    
    
def buymedicine(request,bmid):
    if 'userid' in request.session:
        mo=NewMedicine.objects.get(id=bmid)
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            quan=request.POST.get("quantity")
            topr=request.POST.get("totalprice")
            Bookmedicine.objects.create(quantity=quan,totalprice=topr,user=userobj,medicine=mo)
            return render(request,'User/Buymedicine.html',{"name":mo,"user":userobj})
        else:
         return render(request,'User/Buymedicine.html',{"name":mo,"user":userobj})
    else:
        return redirect('Guest:Login')
    

def contactservice(request,csid):
    if 'userid' in request.session:
        mo=Services.objects.get(id=csid)
        return render(request,'User/Contactservice.html',{"name":mo})
    else:
        return redirect('Guest:Login')



def viewbookproduct(request):
    if 'userid' in request.session:
        med=Bookproduct.objects.filter(product__user=request.session["userid"])
        return render(request,'User/Orders.html',{"product":med})
    else:
        return redirect('Guest:Login')


def acceptedorder(request,psid):
    if 'userid' in request.session:
        medobj=Bookproduct.objects.get(id=psid)
        print(medobj)
        email1=medobj.user.email
        name=medobj.user.name
        obj=medobj.product.id
        newobj=Newproduct.objects.get(id=obj)
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
        return redirect('/User/Viewproduct/')
    else:
        return redirect('Guest:Login')



def rejectedorder(request,rid):
    if 'userid' in request.session:
        medobj=Bookproduct.objects.get(id=rid)
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
        return redirect('/User/Viewproduct/')
    else:
        return redirect('Guest:Login')


def acceptorder(request):
    if 'userid' in request.session:
        ac=Bookproduct.objects.filter(vstatus=1)
        return render(request,'User/Acceptedorder.html',{"product":ac})
    else:
        return redirect('Guest:Login')

def rejectorder(request):
    if 'userid' in request.session:
        ac=Bookproduct.objects.filter(vstatus=2)
        return render(request,'User/Rejectedorder.html',{"product":ac})
    else:
        return redirect('Guest:Login')

def viewmyordermedicines(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        med=Bookmedicine.objects.filter(user=userobj)
        print(med)
        return render(request,'User/Mymedicineorder.html',{"medicine":med})
    else:
        return redirect('Guest:Login')

def viewmyproductorder(request):
    if 'userid' in request.session:
      userobj=Newuser.objects.get(id=request.session["userid"])
      pro=Bookproduct.objects.filter(user=userobj)
      print(pro)
      return render(request,'User/Myproductorder.html',{"product":pro})
    else:
        return redirect('Guest:Login')
    

def payment(request,bmid):
    if 'userid' in request.session:
        bookobj=Bookmedicine.objects.get(id=bmid)
        if request.method=='POST':
            bid=request.POST.get("txthidden")
            bookobj=Bookmedicine.objects.get(id=bid)
            name1=bookobj.user.name
            bookobj.pstatus='1'
            bookobj.save()
            return redirect('User:View-bookproduct')
        else:
            return render(request,'User/Payment.html',{"user":bookobj})
    else:
        return redirect('Guest:Login')
    
def paymentpro(request,bpid):
    if 'userid' in request.session:
        bookobj=Bookproduct.objects.get(id=bpid)
        if request.method=='POST':
            mid=request.POST.get("txthidden")
            bookobj1=Bookproduct.objects.get(id=mid)
            print(bookobj1)
            bookobj1.pstatus='1'
        
            bookobj1.save()
            return redirect('User:View-bookproduct')
        else:
            return render(request,'User/Payment.html',{"user":bookobj})
    else:
        return redirect('Guest:Login')

def logout(request):
    del request.session['userid']
    return redirect('Guest:Login')

def feedback(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST':
            feed=request.POST.get("feedback")
            Feedbackuser.objects.create(Feedback=feed,user=userobj)
            return render(request,'User/Feedbackuser.html')
        else:
         return render(request,'User/Feedbackuser.html')
    else:
        return redirect('Guest:Login')

def help(request,wid):
    if 'userid' in request.session:
        wizardobj=Wizards.objects.get(id=wid)
        userobj=Newuser.objects.get(id=request.session["userid"])
        complaints=Help.objects.filter(user=userobj)
        if request.method=='POST' and request.FILES:
            head=request.POST.get("title")
            dis=request.POST.get("discription")
            pho=request.FILES.get("photo")
            Help.objects.create(title=head,discription=dis,photo=pho,user=userobj,wizard=wizardobj)
            return render(request,'User/Help.html',{"complaints":complaints})
        else:
         return render(request,'User/Help.html',{"complaints":complaints})
    else:
        return redirect('Guest:Login')

def complaintuser(request):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintuser.objects.create(content=con,attachment=att,user=userobj)
            return redirect('/User/Home/')
        else:
            return render(request,'User/complaintuser.html')
    else:
        return redirect('Guest:Login')

def viewmycomplaint(request):
    if 'userid' in request.session:
        com=Complaintuser.objects.filter(user=request.session["userid"],vstatus=0)
        return render(request,'User/Usercomplaintview.html',{"complaint":com})
    else:
        return redirect('Guest:Login')


def complaintproduct(request,pcid):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=pcid)
        userobj1=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintproduct.objects.create(content=con,attachment=att,touser=userobj,fromuser=userobj1)
            return redirect('/User/Home/')
        else:
            return render(request,'User/Complaintproduct.html')
    else:
        return redirect('Guest:Login')

def viewproductcomplaint(request):
    if 'userid' in request.session:
        com=Complaintproduct.objects.filter(user=request.session["userid"],vstatus=0)
        return render(request,'User/Viewproductcomplaint.html',{"complaint":com})
    else:
        return redirect('Guest:Login')

def complaintusertoshop(request,usid):
    if 'userid' in request.session:
        userobj=Newuser.objects.get(id=usid)
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintusertoshop.objects.create(content=con,attachment=att,user=userobj)
            return redirect('/User/Home/')
        else:
            return render(request,'User/Complaintusertoshop.html')
    else:
        return redirect('Guest:Login')

def viewcomplaintusertoshop(request):
    if 'userid' in request.session:
        com=Complaintusertoshop.objects.filter(user=request.session["userid"],vstatus=0)
        return render(request,'User/Viewcomplaintusertoshop.html',{"complaint":com})
    else:
        return redirect('Guest:Login')

def complaintusertodesigner(request,udid):
    if 'userid' in request.session:
        designerobj=Newdeigner.objects.get(id=udid)
        print(designerobj)
        userobj=Newuser.objects.get(id=request.session["userid"])
        if request.method=='POST'and request.FILES:
            con=request.POST.get("content")
            att=request.FILES.get("attachment")
            Complaintusertodesigner.objects.create(content=con,attachment=att,user=userobj,designer=designerobj)
            return redirect('/User/Home/')
        else:
            return render(request,'User/Complaintusertodesigner.html')
    else:
        return redirect('Guest:Login')

def viewcomplaintusertodesigner(request):
    if 'userid' in request.session:
        com=Complaintusertodesigner.objects.filter(user=request.session["userid"],vstatus=0)
        return render(request,'User/Viewcomplaintusertodesigner.html',{"complaint":com})
    else:
        return redirect('Guest:Login')


def replyusertouser(request,cpid):
    obj= Complaintproduct.objects.get(id=cpid)
    if request.method=='POST':
        rep=request.POST.get("reply")
        obj.replay=rep
        obj.vstatus=1
        obj.save()
        return redirect('User:Reply-usercomplaint')
    else:
        return render(request,'User/Replyuser.html')


def Chat(request, cid):
    chatobj = Help.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = Wizards.objects.get(id=cied)
        sobj = Newuser.objects.get(id=request.session["userid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        chat.objects.create(
            from_user=sobj, to_wizards=ciedobj, content=content, to_user=None, from_wizards=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = Wizards.objects.get(id=cid)
    # print(userobj)
    sid = request.session["userid"]
    # print(sid)
    suserobj = Newuser.objects.get(id=request.session["userid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message
    li = [cid, cid]
    # print(chatobj2)  # recived msg
    chatobj = chat.objects.raw(
        "select * from User_chat c inner join Guest_newuser u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_wizards_id=%s or c.to_wizards_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def viewwizard(request):
    # if 'userid' in request.session:
        med=Wizards.objects.all()
        return render(request,'User/Viewwizard.html',{"viewwizard":med})
    # else:
    #     return redirect('Guest:Login')

def deliveringdate(request,bid):
    # if 'userid' in request.session:
        bobj=Bookproduct.objects.get(id=bid)
        if request.method=='POST':
            dated=request.POST.get("date")
            bobj.delivering=dated
            bobj.dstatus='1'
            bobj.save()
            return redirect("User:View-product")
        else:

            return render(request,'User/Date.html',{"viewdate":bobj})
    # else:
    #     return redirect('Guest:Login')
    