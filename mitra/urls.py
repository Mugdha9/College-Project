"""mitra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/',views.signupuser,name='signupuser'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='loginuser'),

    #Dashboard
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard1/',views.dashboard1,name='dashboard1'),


    #PHQ9
    path('phq9test/',views.phq9test1,name='phq9test'),

    #PSYCHOMETRIC TEST
    path('generalized_anxiety/',views.generalized_anxiety1,name='generalized_anxiety'),
    path('panicdisorder/',views.panicdisorder1,name='panicdisorder'),
    path('post_traumaticstress/',views.post_traumaticstress1,name='post_traumaticstress'),
    path('major_depressive/',views.major_depressive1,name='major_depressive'),
    path('manic_episodes/',views.manic_episodes1,name='manic_episodes'),

    #PROGRESS REPORT
    path('progress_report/',views.progress_report1,name='progress_report'),

    #Home
    path('',views.home,name='home'),

    #Logout
    path('logoutuser/',views.logoutuser,name='logoutuser'),
]
