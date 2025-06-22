from django.urls import path
from account import views
urlpatterns = [
    path('',views.index),
    path('mba/',views.mba, name="mba"),
    path('bca/',views.bca, name="bca"),
    path('bba/',views.bba, name="bba"),
    path('bcom/',views.bcom, name="bcom"),
    path('bcomhr/',views.bcomhr, name="bcomhr"),
    path('faculty/',views.faculty, name="faculty"),
    path("login/",views.user_login, name="login"),
    path("sign/",views.sign_up, name="sign"),
    path("logout/",views.user_logout, name="logout"),
    path("gallery/",views.gallery_, name="gallery"),
    path("contact",views.contact, name="contact"),
    path("Institute/",views.Institute,name="Institute"),    
    path("international/",views.international,name="international"),    
    path("welcome/",views.welcome,name="welcome"),    
    path("eprakash/",views.eprakash,name="eprakash"),    
    path("pace/",views.pace,name="pace"),    
]