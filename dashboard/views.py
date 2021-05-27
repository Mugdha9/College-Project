from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import phq9form
from .models import phq9test
from .forms import generalized_anxietyform
from .models import generalized_anxiety
from .forms import panicdisorderform
from .models import panicdisorder
from .forms import post_traumaticstressform
from .models import post_traumaticstress
from .forms import major_depressiveform
from .models import major_depressive
from .forms import manic_episodesform
from .models import manic_episodes
from .forms import userForm


def home(request):
    return render(request,'dashboard/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request,'dashboard/signupuser.html',{'form':userForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'],email = request.POST['email'],first_name = request.POST['first_name'],last_name = request.POST['last_name'])
                #user = userForm(request.POST)
                user.save()
                login(request,user)
                return redirect('dashboard1')
            except IntegrityError:
                return render(request,'dashboard/signupuser.html',{'form':userForm(),'error':'This username has already been taken'})

        else:
            return render(request,'dashboard/signupuser.html',{'form':userForm(),'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'dashboard/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'dashboard/loginuser.html',{'form':AuthenticationForm(),'error':'Username and password do not match'})
        else:
            login(request,user)
            #return render(request,'dashboard/dashboard1.html',{'user':request.user})
            return redirect('dashboard1')


def logoutuser(request):
    #if request.method == 'POST':
        logout(request)
        return redirect('home')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def dashboard1(request):
    return render(request,'dashboard/dashboard1.html')

def phq9test1(request):
    if request.method == 'GET':
        return render(request,'dashboard/phq9test.html',{'form':phq9form()})
    else:
        try:
            form = phq9form(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans9 = int(request.POST.get('ans9'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8 + ans9;
            if ans>=0 and ans<=4:
                category = 'A'
            elif ans>=5 and ans<=9:
                category = 'B'
            elif ans>=10 and ans<=14:
                category = 'C'
            elif ans>=15 and ans<=19:
                category = 'D'
            elif ans>=20 and ans<=27:
                category = 'E'
            newtest = phq9test.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,ans9 = ans9,total_score = ans,user = request.user,category = category,user1 = request.user)
            newtest.save()
            return redirect('dashboard1')
        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})

def generalized_anxiety1(request):
    if request.method == 'GET':
        return render(request,'dashboard/psychometrictest/generalized_anxiety.html',{'form':generalized_anxietyform()})
    else:
        try:
            form = generalized_anxietyform(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8;
            newtest = generalized_anxiety.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,total_score = ans,user = request.user,percentage = (ans/32)*100,user1 = request.user)
            newtest.save()
            return redirect('panicdisorder')

        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})

def panicdisorder1(request):
    if request.method == 'GET':
        return render(request,'dashboard/psychometrictest/panicdisorder.html',{'form':panicdisorderform()})
    else:
        try:
            form = panicdisorderform(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8;
            newtest = panicdisorder.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,total_score = ans,user = request.user,percentage = (ans/24)*100,user1 = request.user)
            newtest.save()
            return redirect('post_traumaticstress')
        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})

def post_traumaticstress1(request):
    if request.method == 'GET':
        return render(request,'dashboard/psychometrictest/post_traumaticstress.html',{'form':post_traumaticstressform()})
    else:
        try:
            form = post_traumaticstressform(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8;
            newtest = post_traumaticstress.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,total_score = ans,user = request.user,percentage = (ans/8)*100,user1 = request.user)
            newtest.save()
            return redirect('major_depressive')
        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})


def major_depressive1(request):
    if request.method == 'GET':
        return render(request,'dashboard/psychometrictest/major_depressive.html',{'form':major_depressiveform()})
    else:
        try:
            form = major_depressiveform(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8;
            newtest = major_depressive.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,total_score = ans,user = request.user,percentage = (ans/24)*100,user1 = request.user)
            newtest.save()
            return redirect('manic_episodes')
        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})

def manic_episodes1(request):
    if request.method == 'GET':
        return render(request,'dashboard/psychometrictest/manic_episodes.html',{'form':manic_episodesform()})
    else:
        try:
            form = manic_episodesform(request.POST);
            ans1 = int(request.POST.get('ans1'));
            ans2 = int(request.POST.get('ans2'));
            ans3 = int(request.POST.get('ans3'));
            ans4 = int(request.POST.get('ans4'));
            ans5 = int(request.POST.get('ans5'));
            ans6 = int(request.POST.get('ans6'));
            ans7 = int(request.POST.get('ans7'));
            ans8 = int(request.POST.get('ans8'));
            ans = ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8;
            newtest = manic_episodes.objects.create(ans1 = ans1,ans2 = ans2,ans3 = ans3,ans4 = ans4,ans5 = ans5,ans6 = ans6,ans7 = ans7,ans8 = ans8,total_score = ans,user = request.user,percentage = (ans/24)*100,user1 = request.user)
            newtest.save()
            return redirect('progress_report')

        except IntegrityError:
            return render(request,'dashboard/integrityerror.html',{'error':'You have already taken the test.'})

def progress_report1(request):
    ga_result = generalized_anxiety.objects.get(user = request.user)
    pd_result = panicdisorder.objects.get(user = request.user)
    pt_result = post_traumaticstress.objects.get(user = request.user)
    md_result = major_depressive.objects.get(user = request.user)
    me_result = manic_episodes.objects.get(user = request.user)
    return render(request,'dashboard/psychometrictest/progress_report.html',{'ga_result':ga_result,'pd_result':pd_result,'pt_result':pt_result,'md_result':md_result,'me_result':me_result})
