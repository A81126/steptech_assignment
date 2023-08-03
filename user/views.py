from django.shortcuts import render,redirect
from .models import Data_Users

# Create your views here.

def home(request):
    user=Data_Users.objects.all()
    return render(request,"user/home.html",{'user':user})



def hello(request):
    
    return render(request,"user/hello.html",{})

def user_add(request):
    if request.method=='POST':
        print("ashish")
        # retretive the user data
        users_id=request.POST.get("user_id")
        users_name=request.POST.get("user_name")
        users_email=request.POST.get("user_email")
        users_roll=request.POST.get("user_roll")
        
        # create an object
        d=Data_Users()
        d.id=users_id
        d.name=users_name
        d.email=users_email
        d.roll=users_roll
        
        d.save()
        return redirect("/user/users")
    
    
    return render(request,"user/add_user.html",{})


def user_search(request,id):
    user=Data_Users.object.get(pk=id)
    return render(request,"user/home.html",{'user':user})



