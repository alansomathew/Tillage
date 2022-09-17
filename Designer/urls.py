

from django.urls import path

from Designer import views


app_name="Designer"


urlpatterns = [
    path('Home/',views.homepage,name="Designer-Home"),
    path('myprofile/',views.Myprofile,name="my-profile"),
    path('editprofile/',views.editprofile,name="edit-profile"),
    path('changepassword/',views.changepassword,name="change-password"),  
    path('Services/',views.services,name="Add-Services"),
    path('DelServices/<int:mid>/',views.delservice,name="del-Services"),
    path('Logout/',views.logout,name="logout"),
    path('Feedback/',views.feedback,name="Feedback Designer"),
    path('Complaintdesigner/',views.complaintdesigner,name="Complaint Designer"),
    path('Viewcomplaintdesigner/',views.viewcomplaintdesigner,name="Viewcomplaint Designer"),
    path('Viewusercomplaint/',views.viewcomplaintuserdesigner,name="Viewcomplaint user"),
    path('Replyusercomplaint/<int:rdid>/',views.replyusertodesigner,name="Replycomplaint user"),



]