from django.shortcuts import redirect, render
from django.http import HttpRequest
from ninjas.models import Ninja,User
from missions.models import Client
from datetime import date,datetime

#pagina principal
def index(request):
    return render(request,'seven_ways_net/index.html',{})



#registro de usuarios
def register(request :HttpRequest):
    return render(request,'seven_ways_net/register.html',{'errors':None}) #ver como obtener los errores al no poder registrar un usuario...

def endRegister(request :HttpRequest):
    username=request.POST.get("username")
    password=request.POST.get("password")
    errors = []
    if verify_existence(username): 
        errors.append("The user name exists.")
        return redirect('register',) #ver como pasar los errores a register, para poder mostrarlos
        
    user = User(username = username)
    user.set_password(password)

    userType=request.POST.get("userType")
    name =  request.POST.get("name")
    if (userType == "ninja"):
        clan=request.POST.get("clan")
        birth_date =  request.POST.get("birthdate")
        birth_date = date.fromisoformat(birth_date)
        gender =  request.POST.get("gender")
        user.save()
        Ninja(name=name, age = calc_age(birth_date),clan=clan, birth_date = birth_date,gender = gender, user=user).save()
    else:
        country=request.POST.get("country")
        user.save()
        Client(name=name,user=user,country=country).save()
    
    return redirect("/auth/login")


#---------- 
def verify_existence(username):
    return len(User.objects.filter(username = username))

def calc_age(birth_date):
    return (datetime.now().date() - birth_date).days//365
