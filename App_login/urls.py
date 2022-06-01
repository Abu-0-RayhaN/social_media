from django.urls import path
from App_login import views
app_name='App_login'
urlpatterns = [
    path('authsignup/',views.sign_up,name="authsignup"),
    path('authlogin/', views.authlogin,name="authlogin"),
    path('authlogout/',views.logout_user,name="authlogout"),
    path('editprofile/',views.editprofile,name="editprofile"),
    
    
    
]
