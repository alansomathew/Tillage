from django.shortcuts import render,redirect

from Admin.models import Wizards
from Guest.models import Newuser
from User.models import Help, chat
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def homepage(request):
    if 'wizardid' in request.session:
        return render(request,'Wizards/Home.html')
    else:
        return redirect('Guest:Login')


def Myprofile(request):
    if 'wizardid' in request.session:
        wizardobj=Wizards.objects.get(id=request.session["wizardid"])
        return render(request,'Wizards/Myprofile.html',{"wizard":wizardobj})
    else:
        return redirect('Guest:Login')

def editprofile(request):
        wizardobj=Wizards.objects.get(id=request.session["wizardid"])
        if request.method=='POST':
            name=request.POST.get("name")
            contact=request.POST.get("contact")
            address=request.POST.get("address")
            wizardobj.name=name
            wizardobj.contact=contact
            wizardobj.address=address
            wizardobj.save()
            return redirect('Wizard:my-profile')
        else:
            return render(request,'Wizards/Editprofile.html',{"user":wizardobj})

def changepassword(request):
    # if 'userid' in request.session:
        wizardobj=Wizards.objects.get(id=request.session["wizardid"])
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
            return render(request,'Wizards/Changepassword.html')
    # else:
    #     return redirect('Guest:Login')


def viewcompaint(request):
    # if 'shopid' in request.session:
        com=Help.objects.all()
        return render(request,'Wizards/Viewcomplaints.html',{"complaints":com})
    # else:
    #     return redirect('Guest:Login')

def accepthelp(request,aid):
    # if 'shopid' in request.session:
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
        return redirect('Wizards:View-complaint')
    # else:
    #     return redirect('Guest:Login')


def rejecthelp(request,rid):
    # if 'shopid' in request.session:
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
        return redirect('Wizards:View-complaint')
    # else:
    #     return redirect('Guest:Login')



def viewaccepthelp(request):
    # if 'adminid' in request.session:
        acuser=Help.objects.filter(vstatus=1)
        return render(request,'wizards/Acceptedhelp.html',{"user":acuser})
    # else:
    #     return redirect('Guest:Login')


def viewrejecthelp(request):
    # if 'adminid' in request.session:
        acuser=Help.objects.filter(vstatus=2)
        return render(request,'wizards/Rejectedhelp.html',{"user":acuser})
    # else:
    #     return redirect('Guest:Login')

def logout(request):
    del request.session['wizardid']
    return redirect('Guest:Login')


def Chat(request, cid):
    chatobj = Help.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = Newuser.objects.get(id=cied)
        sobj = Wizards.objects.get(id=request.session["wizardid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        chat.objects.create(
            from_user=None, to_wizards=None, content=content, to_user=ciedobj, from_wizards=sobj)
        return render(request, 'Wizards/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'Wizards/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = Newuser.objects.get(id=cid)
    # print(userobj)
    sid = request.session["wizardid"]
    # print(sid)
    suserobj = Wizards.objects.get(id=request.session["wizardid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message
    li = [cid, cid]
    # print(chatobj2)  # recived msg
    chatobj = chat.objects.raw(
        "select * from User_chat c inner join Admin_wizards u on (u.id=c.from_wizards_id) or (u.id=c.to_wizards_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Wizards/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})

