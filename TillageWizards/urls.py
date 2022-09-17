from django.urls import path
from Admin.views import medicinecat
from TillageWizards import views

app_name="TillageWizards"


urlpatterns = [
    path('Home/',views.homepage,name="wizards-home"),
    path('myprofile/',views.Myprofile,name="my-profile"),
    path('editprofile/',views.editprofile,name="edit-profile"),
    path('changepassword/',views.changepassword,name="change-password"),
    path('Addproduct/',views.addproduct,name="Add-product"),
    path('Acceptedorder/',views.acceptorder,name="Acceptorder"),
    path('Rejectedorder/',views.rejectorder,name="Rejectorder"),
    path('Addstock/<int:eid>/',views.addstock,name="Add-stock"),
    path('deleteproduct/<int:mid>/',views.delproduct,name="del-product"),
    path('Acceptmedicine/<int:aid>/',views.acceptmedicine,name="Accepted-medicine"),
    path('Rejectedmedicine/<int:rid>/',views.rejectmedicine,name="Rejected-medicine"),
    path('Viewmedicine/',views.viewbookmedicines,name="View-Orders"),
    path('Logout/',views.logout,name="logout"),
    path('Feedback/',views.feedback,name="Feedback-Wizards"),
    path('ViewHelp/',views.viewcompaint,name="View-complaints"),
    path('Accepthelp/<int:aid>/',views.accepthelp,name="Accept-help"),
    path('Rejecthelp/<int:rid>/',views.rejecthelp,name="reject-help"),
    path('Setconsultationfee/<int:cid>/',views.addconsulationfee,name="Set-Consultationfee"),
    path('Complaintshop/',views.complaintshop,name="shop-complaints"),
    path('Viewcomplaintshop/',views.viewcomplaintwizard,name="viewshop-complaints"),
    path('Viewcomplaintuser/',views.viewcomplaintusertoshop,name="viewuser-complaints"),
    path('Replycomplaintuser/',views.viewcomplaintusertoshop,name="Replyuser-complaints"),
]





