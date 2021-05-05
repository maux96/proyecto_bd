from django.shortcuts import render

def index(request):
    context= {
        "title": "Home",
        "header": "Pagina Principal"
    }
    return render(request,'seven_ways_net/index.html',context)