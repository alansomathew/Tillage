
from django.urls import path

from User import views

app_name="User"


urlpatterns = [
    path('Home/',views.homepage,name="User-Home"),
    path('myprofile/',views.Myprofile,name="my-profile"),
    path('editprofile/',views.editprofile,name="edit-profile"),
    path('changepassword/',views.changepassword,name="change-password"),
    path('Addsalesproduct/',views.product,name="Add-product"),
    path('Addstock/<int:eid>/',views.addstock,name="Add-stock"),
    path('Viewproduct/',views.viewbookproduct,name="View-product"),
    path('Viewbookmedicine/',views. viewmyordermedicines,name="View-bookmedicine"),
    path('Viewbookproduct/',views. viewmyproductorder,name="View-bookproduct"),
    path('Acceptedproduct/<int:psid>/',views.acceptedorder,name="Accepted-order"),
    path('Rejectedproduct/<int:rid>/',views.rejectedorder,name="Rejected-order"),
    path('deleteproduct/<int:pid>/',views.delproduct,name="del-product"),
    path('Searchproduct/',views.searchproduct,name="Search-product"),
    path('Searchmedicine/',views.searchmedicine,name="Search-medicine"),
    path('Searchservices/',views.searchservice,name="Search-services"),
    path('Viewmoreservices/<int:sid>/',views.viewmoreservice,name="viewmore-services"),
    path('Viewmoreproduct/<int:pid>/',views.viewmoreproduct,name="viewmore-product"),
    path('Viewmoremedicine/<int:mid>/',views.viewmoremedicine,name="viewmore-medicine"),
    path('Buyproduct/<int:bpid>/',views.buyproduct,name="Buy-product"),
    path('Buymedicine/<int:bmid>/',views.buymedicine,name="Buy-medicine"),
    path('Contactservice/<int:csid>/',views.contactservice,name="Contact-service"),
    path('Payment/<int:bmid>/',views.payment,name="Pay-now"),
    path('Paymentpro/<int:bpid>/',views.paymentpro,name="Pay-nowpro"),
    path('Logout/',views.logout,name="logout"),
    path('Feedback/',views.feedback,name="Send Feedback"),
    path('Help/<int:wid>/',views.help,name="help-help"),
    path('Complaintuser/',views.complaintuser,name="send-complaint"),
    path('Viewcomplaintuser/',views.viewmycomplaint,name="Viewuser-complaint"),
    path('Complaintproduct/<int:pcid>/',views.complaintproduct,name="Send-productcomplaint"),
    path('Complaintusertoshop/<int:usid>/',views.complaintusertoshop,name="Send-shopcomplaint"),
    path('Complaintusertodesigner/<int:udid>/',views.complaintusertodesigner,name="Send-designercomplaint"),
    path('Replayusertouser/<int:rpid>/',views.replyusertouser,name="Reply-usercomplaint"),
    path('Chats/<int:cid>/',views.Chat,name="Consultations"),
    path('Loadchat/',views.loadchat,name="loadchat"),
    path('Date/<int:bid>/',views.deliveringdate,name="Delivering date"),
    path('Viewwizard/',views.viewwizard,name="View-wizard"),






]


