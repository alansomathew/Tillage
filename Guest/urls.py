from pydoc import visiblename
from unicodedata import name
from django.urls import path
from Admin.views import acceptdesigner, rejectdesigner

from Guest import views
app_name="Guest"

urlpatterns = [
    path('Newuser/',views.newuser,name="Newuser"),
    path('Newshop/',views.newshop, name="Newshop"),
    path('Newdesigner/',views.newdesigner,name="Newdesigner"),
    path('loadplace/',views.loadplace,name="load-place"),
    path('Login/',views.login,name="Login"), 
    
  
]