from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def About(request):
    return render(request,'about.html')
def Contact(request):
    return render(request,'contact.html')
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointment= Appointment.objects.all()

    d= 0;
    p= 0;
    a = 0;
    for i in doctors:
        d+=1
    for j in patients:
         p+=1
    for k  in appointment:
        a+= 1
    d1 = {'d':d,'p':p,'a':a}

    return render(request,'index.html',d1)

def Login(request):
    error = ""
    if request.method == 'POST':
        u =  request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u , password = p)
        try:

            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error ="yes"
        except:
            error = "yes"

    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n =  request.POST['name']
        c = request.POST['contact']
        s= request.POST['special']
      
        try:

            Doctor.objects.create(name=n,mobile=c,special=s)
            error ="no"
            
        except:
            error = "yes"

    d = {'error':error}
    return render(request,'add_doctor.html',d)
def Delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all(id=pid)
    doctor.deleted()
    return redirect('view_doctor')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)




def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n =  request.POST['name']
        c = request.POST['mobile']
        g = request.POST['gender']
        a = request.POST['address']
      
        try:

            Patient.objects.create(name=n,mobile=c,gender=g,address=a)
            error ="no"
            
        except:
            error = "yes"

    d = {'error':error}
    return render(request, 'add_patient.html', d)
    

def Delete_Patient(request,rid):
     if not request.user.is_staff:
        return redirect('login')
     Patient= Patient.objects.get(id = rid)
     Patient.delete()
     return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)




def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d1=  request.POST['doctor']
        p1 = request.POST['patient']
        d2 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name = d1).first()
        patient = Patient.objects.filter(name = p1).first()

      
        try:

            Appointment.objects.create(doctor =doctor,patient =patient,date1 = d2,time1 = t)
            error ="no"
            
        except:
            error = "yes"

    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request, 'add_appointment.html', d)
    

def Delete_Appointment(request,rid):
     if not request.user.is_staff:
        return redirect('login')
     appointment= Appointment.objects.get(id = rid)
     appointment.delete()
     return redirect('view_appointment')