
from django.urls import path

from Wizards import views

app_name="Wizards"


urlpatterns = [
    path('Home/',views.homepage,name="WizardsHome"),
    path('myprofile/',views.Myprofile,name="my-profile"),
    path('Editprofile/',views.editprofile,name="Edit-profile"),
    path('Changepassword/',views.changepassword,name="Change-password"),
    path('Viewcomplaint/',views.viewcompaint,name="View-complaint"),
    path('Accepthelp/<int:aid>/',views.accepthelp,name="Accept-Help"),
    path('Rejecthelp/<int:rid>/',views.rejecthelp,name="Reject-Help"),
    path('ViewAccepthelp/',views.viewaccepthelp,name="ViewAccept-Help"),
    path('ViewRejecthelp/',views.viewrejecthelp,name="ViewReject-Help"),
    path('Logout/',views.logout,name="Logout"),
    path('Chats/<int:cid>/',views.Chat,name="Chat-User"),
    path('Loadchat/',views.loadchat,name="loadchat"),
    

]