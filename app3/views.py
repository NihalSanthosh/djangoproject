from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as logouts
from app3.forms import GalleryForm, LoginForm,RegisterForm,UpdateForm,PasswordChangeForm,GalleryForm
from . models import Negister,Gallery
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']
            
            chk=Negister.objects.filter(Email=email).exists()
            
            if chk:
                messages.warning(request,"Email already exist")
                return redirect('/register')
            elif password!=cpassword:
                messages.warning(request,"Password mismatch")
                return redirect('/register')
            else:
                tab=Negister(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()  
                messages.success(request,"success")
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'data':form})


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            
            chk=Negister.objects.get(Email=email)
            
            if not chk:
                messages.warning(request,"Email does not exist")
                return redirect('/login')
            elif password!=chk.Password:
                messages.warning(request,"Password incorrect")
                return redirect('/login')
            else: 
                messages.success(request,"login success")
                return redirect('/home/%s' % chk.id )
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})

def home(request,id):
    user=Negister.objects.get(id=id)
    return render(request, 'home.html',{'user':user})

def update(request,id):
    user=Negister.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            # name=form.cleaned_data['Name']
            # age=form.cleaned_data['Age']
            # place=form.cleaned_data['Place']
            # email=form.cleaned_data['Email']
            form.save()
            messages.success(request,"updated successfully")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})

            
def view_users(request):
    users=Negister.objects.all()
    return render(request,'view_users.html',{'users':users}) 

def remove_user(request,id):
    user=Negister.objects.get(id=id)
    user.delete()
    messages.success(request,"deleted successfully")
    return redirect('/view_users')

def password_change(request,id):
    user=Negister.objects.get(id=id)
    if request.method=='POST':
        form=PasswordChangeForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            if oldpassword!= user.Password:
                messages.warning(request,"incorrect password")
                return redirect('/password_change/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"old and new password could not be same")
                return redirect('/password_change/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"confirm password did not match")
                return redirect('/password_change/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"password changed successfully")
                return redirect('/home/%s' % user.id)
    else:
        form=PasswordChangeForm()
    return render(request,'changepassword.html',{'data':form,'user':user})

def logout(request):
    logouts(request)
    messages.success(request,"Loged out successfully")
    return redirect('/')

def gallery(request):
    if request.method=='POST':
        form=GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully imported")
            return redirect('/')
    else:
        form=GalleryForm()
    return render(request, 'gallery.html', {'data':form})