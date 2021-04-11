from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .forms import StudentRegistration
from .models import Empid
from qrcode import *
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")
    

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        mob=request.POST['mob']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input

        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        

        if (pass1!= pass2):
             messages.error(request, "Your password not matching")
             return redirect('/')

        if len(mob)!=10:
            messages.error(request, "enter valid Mobile No")
            return redirect('/')     
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.mob= mob
        myuser.save()
        messages.success(request, "You have been successfully registered please login by useing your username and password")
        
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")


def lhome(request):
    return render(request,'loginhome.html')
    
data=None
nm=None
# Create your views here.
def home(request):
    if request.method=='POST' :   
        global nm  
        fm=StudentRegistration(request.POST )
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            p=fm.cleaned_data['post']
            bg=fm.cleaned_data['bloodgroup']
            reg=Empid(name=nm,email=em,post=p,bloodgroup=bg)
            reg.save()
            fm=StudentRegistration()

            # --------------------------------
            global data
           
            info={'name':nm,'email':em,'post':p,'bg':bg}
            data=str(info)
            img = make(data)
            # img.save("static/image/test.png")
            img.save('static/image/'+nm+'.png')
            
        else:
            pass
        return render(request,"qrcode.html",{'name':nm})    
           

    if request.method=='GET':
         fm=StudentRegistration() 

    return render(request,'addandshow.html',{'form':fm})


def showinfo(request):
    semp=Empid.objects.all()
    # print(semp)
    context={'semp': semp}
    # print(context)
    return render(request, 'showinfo.html',context)

    
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')