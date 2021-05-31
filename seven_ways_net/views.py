from skills.models import Skill
from django.shortcuts import redirect, render
from django.http import HttpRequest
from ninjas.models import ChuninNinja, GeninNinja, JouninNinja, Ninja,User
from missions.models import Mission
from missions.models import Client
from datetime import date,datetime

#pagina principal
def index(request):
    best5Reward = Best5RewardMissions()
    ninjaInvocationPair = NinjaInvocationPair()
    jounin3C = ShowJouninsWith3C()
    medicCapitans = MedicCapitans()
    exposedSkills = ExposedSkills()
    return render(request,'seven_ways_net/index.html',{ 
                                                        "femalePercent":femalePercent(),
                                                        "best5Reward" : best5Reward,
                                                        "ninjaInvocationPair":ninjaInvocationPair,
                                                        "jounin3C":jounin3C,
                                                        "medicCapitans":medicCapitans,
                                                        "exposedSkills":exposedSkills
                                                        })



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
        ninjaType = request.POST.get("ninjaType")
        graduation_date = request.POST.get("graduationdate")
        calification = request.POST.get("calification")
        
        user.save()
        if ninjaType == "genin":            
            GeninNinja(name=name, age = calc_age(birth_date),clan=clan, birth_date = birth_date,gender = gender, user=user,graduation_date = graduation_date,assessment = calification).save()    
        elif ninjaType == "chunin":
            ChuninNinja(name=name, age = calc_age(birth_date),clan=clan, birth_date = birth_date,gender = gender, user=user,exam_date = graduation_date,classification = calification).save()    
        elif ninjaType == "jounin":
            JouninNinja(name=name, age = calc_age(birth_date),clan=clan, birth_date = birth_date,gender = gender, user=user,exam_date = graduation_date,classification = calification).save()    
    else:
        country=request.POST.get("country")
        user.save()
        Client(name=name,user=user,country=country).save()
    
    return redirect("/auth/login")

#---------

def femalePercent():
    total_famale = len(Ninja.objects.filter(gender="F"))
    total = len(Ninja.objects.all())
    return (total_famale/total )*100
def Best5RewardMissions():
    return Mission.objects.order_by("-reward")[:5]
def NinjaInvocationPair():          #falta poner que solo los que tengan mas de 6 misiones con rango S.
    ninjas = Ninja.objects.all()
    sol=[]
    for n in ninjas:
        for i in n.invocations.all():
            sol.append((n,i))
    return sol
def ShowJouninsWith3C():
    jounins = JouninNinja.objects.filter(mission__rank__lte="C")
    sol = set()
    for j in jounins:
        c=j.mission_set.count()
        if c >= 3: 
            sol.add((j,c))
    return list(sol)

def MedicCapitans():
    jounins = JouninNinja.objects.filter(is_medic=True)
    sol = set()
    for j in jounins:
        c = j.mission_set.count()
        if c != 0:
            sol.add((j,c))
    return list(sol)
def ExposedSkills():
    skills=Skill.objects.filter(belong_to_the_village=True).exclude(ninja__team__mission__client__country="Fire").exclude(ninja__team__mission__isnull=True)
    return skills


#---------- 
def verify_existence(username):
    return len(User.objects.filter(username = username))

def calc_age(birth_date):
    return (datetime.now().date() - birth_date).days//365
