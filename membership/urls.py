from django.urls import path
from django.urls.conf import include   
from django.conf import settings  
from django.conf.urls.static import static  
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("home/", views.home, name="home"),
path("adminpage/", views.admin_view, name="adminpage"),
path("monthlyform/", views.monthly_form, name="monthlyform"),
path("signup/", views.signup_view, name="signup"),
path("signin/", views.signin_view, name="signin"),
path("signout/", views.signout_view, name="signout")
# path("logout/", views.logout_view, name="logout"),
# path("index/", views.index, name="index"),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  