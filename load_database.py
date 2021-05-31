#OBSOLETO!!

from ninjas.models import ChuninNinja, JouninNinja, Team, User
from missions.models import Mission,MissionResult,Client
from datetime import datetime,date

from os import remove,system

def Execute():
    print("ESTE ARCHIVO YA ESTA OBSOLETO!!!")
    desition=input("Seguro que quieres eliminar la base de datos que con tanto amor llenaste y retornarla a los valores por defecto??  (y/N)  ")
    if desition != "y":
        print("Cancelado.")
        return

    print("Retornando la base de datos a sus valores por defecto...\n")
    remove('db.sqlite3')
    system("python3 manage.py migrate")

    """ Aqui poner todo lo que se va a agregar a la base de datos por defecto... """

    n=User(username="naruto")
    n.set_password("naruti1234")
    s=User(username="sasuke")
    s.set_password("sasuki1234")
    sa=User(username="sakura")
    sa.set_password("saku1234")
    k= User(username="kakashi")
    k.set_password("kaka1234")
    n.save()
    s.save()
    sa.save()
    k.save()
    t7= Team(name = "7")
    t7.save()

    ChuninNinja(name="Naruto",age=20,clan="Uzumaki",birth_date=datetime(2000,3,12,12,0,0,0),gender="M",user=n,team=t7,exam_date=date(2018,5,23),classification=3 ).save()
    ChuninNinja(name="Sasuke",age=20,clan="Uchiha",birth_date=datetime(2000,4,10,12,0,0,0),gender="M",user=s,team=t7,exam_date=date(2018,5,23),classification=5).save()
    ChuninNinja(name="Naruto",age=20,clan="Haruno",birth_date=datetime(2000,2,15,12,0,0,0),gender="F",user=sa,team=t7,exam_date=date(2018,5,23),classification=5).save()
    k= JouninNinja(name="Kakashi",age=20,clan="Hatake",birth_date=datetime(2000,3,12,12,0,0,0),gender="M",user=k,exam_date=date(2009,5,23),classification=5)
    k.save()


    g=User(username="godofredo")
    g.set_password("godo1234")
    g.save()
    g=Client(name="Godofredo", country = "Fire",user=g)
    g.save()
    m=Mission(name="Buscar el Pan",description="Ir a la aldea de la arena a quitarle el pan a Gaara",rank="S",reward=300,available=True,client=g,team=t7,leader=k)
    m.save()
    MissionResult(result = "Done",begin_date = date(2020,5,23),end_date = date(2020,7,10),mission=m).save()

    """ ... """

    print("\nDone.")
    print("Recuerda crear el superusuario Admin.")