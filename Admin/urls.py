from Admin import views
from django.urls import path

app_name="Admin"

urlpatterns = [
     path('Myprofile/',views.Myprofile,name="My-profile"),
    path('District/',views.dis,name="District"),
    path('Place/',views.pl,name="Place"),
    path('Category/',views.cat,name="Category"),
    path('User/',views.viewuser,name="User"),
    path('Shop/',views.viewshop,name="Shop"),
    path('Designer/',views.viewdesigner,name="Designer"),
    path('Rejecteduser/',views.viewrejectuser,name="Rejectuser"),
    path('Rejectedshop/',views.viewrejectshop,name="Rejectshop"),
    path('Rejecteddesigner/',views.viewrejectdesigner,name="Rejectdesigner"),
    path('Acceptshop/',views.accshop,name="AcceptShop"),
    path('Acceptuser/',views.accuser,name="Acceptuser"),
    path('Acceptdesigner/',views.accdesigner,name="Acceptdesigner"),
    path('deldistrict/<int:disid>/',views.deldis,name="del-dis"),
    path('editdistrict/<int:eid>/',views.editdis,name="edit-dis"),
    path('delplace/<int:pid>/',views.delpl,name="del-place"),
    path('delcategory/<int:cid>/',views.delcat,name="del-cat"),
    path('editcategory/<int:cid>/',views.editcat,name="edit-cat"),
    path('Acceptuser/<int:aid>/',views.acceptuser,name="Accepted-user"),
    path('Rejectuser/<int:rid>/',views.rejectuser,name="Rejected-user"),
    path('Acceptshop/<int:aid>/',views.acceptshop,name="Accepted-shop"),
    path('Rejectshop/<int:rid>/',views.rejectshop,name="Rejected-shop"),
    path('Acceptdesigner/<int:aid>/',views.acceptdesigner,name="Accepted-designer"),
    path('Rejectdesigner/<int:rid>/',views.rejectdesigner,name="Rejected-designer"),
    path('Medicinecategory/',views.medicinecat,name="Medicinecategory"),
    path('Delmedicinecat/<int:mcid>/',views.delmedicinecat,name="del-medicinecat"),
    path('Editmedicinecat/<int:meid>/',views.editmedicinecat,name="edit-medicinecat"),
    path('Viewuserfeedback/',views.viewfeedbackuser,name="UserFeedback"),
    path('Viewdesignerfeedback/',views.viewfeedbackdesigner,name="DesignerFeedback"),
    path('Viewwizardsfeedback/',views.viewfeedbackshop,name="shopFeedback"),
    path('Viewusercomplaint/',views.viewcomplaintuser,name="Usercomplaint"),
    path('Viewdesignercomplaint/',views.viewcomplaintdesigner,name="Designercomplaint"),
    path('Viewshopcomplaint/',views.viewcomplaintshop,name="Shopcomplaint"),
    path('Homepage/',views.homepage,name="Home"),
    path('Replyuser/<int:cid>/',views.replyuser,name="reply-user"),
    path('Replyshop/<int:rsid>/',views.replyshop,name="reply-shop"),
    path('Replydesigner/<int:rdid>/',views.replydesigner,name="reply-designer"),
    path('ReplyWizards/<int:rdid>/',views.replywizards,name="reply-wizards"),
    path('Addwizards/',views.wizards,name="Addwizards"),
    path('Logout/',views.logout,name="Logout"),
    
    

]



    
    

