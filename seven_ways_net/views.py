from django.shortcuts import render

#pagina principal
def index(request):
    return render(request,'seven_ways_net/index.html',{})

#registro de usuarios
def register(request):
    return render(request,'seven_ways_net/register.html',{})