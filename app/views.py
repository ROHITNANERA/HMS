from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from requests import session
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import Q


def index(request):
    # return HttpResponse("<h1>Hello, world. You're at the  index.</h1>")
    return render (request,"app/index.html")

def home(request):
   return render(request, 'app/home.html', {})

# def is_login(request):
#     try:
#         return True if (request.session['login']) else False
#     except KeyError:
#         return False

def register(request):
    if request.POST:
        print(request.POST)
        if request.POST['psw'] == request.POST['psw-repeat']:
            print("PAssword is same.")

            hadmin = HAdmin.objects.create()
            hadmin.name = request.POST['name']
            hadmin.email = request.POST['email']
            hadmin.Password = request.POST['psw']
            hadmin.save()
            # return render(request,'app/login.html',{})        #it gives multiple dictionary key errors because password key is used in both login and register and render method does not reset post request.
            return redirect(reverse('login'))
    return render(request, 'app/register.html', {})

def login(request):
    # context = {'form': LoginForm}
    # if request.POST:
    #     print(request.POST)
    #return context in place of '{}' if umcomment this
    try:
        if request.session['login']:
            return render(request,'app/selecthostel.html',{})
    except KeyError:

        if request.POST:
            print(request.POST)
            try:
                hadmin = HAdmin.objects.get(email = request.POST['email'])
                if hadmin.Password == request.POST['psw']:
                    request.session['login']=hadmin.id
                    request.session['islogin'] = True
                    print(request.session['login'])
                    # return render(request,'app/dashboard.html',{})
                    return redirect(reverse("selectforall"))
            
            except ObjectDoesNotExist:
                print("Object does not excist")
        return render(request, 'app/login.html',{})
        # return redirect(reverse('login'))

#for logout option
def logout(request):
    
    request.session.flush()
        # return render(request,'app/login.html',{})
    return redirect(reverse('login'))


def dashboard(request):
    
    try:
        return render(request, 'app/dashboard.html', {}) if request.session['login'] else render(request, 'app/login.html', {})
    except KeyError:
        return redirect(reverse('login'))



def addhostel(request):
        if not request.session['islogin']:
            return redirect(reverse('login'))
    # if is_login(request):
        if request.POST:
            print(request.POST)
            hostel = Hostel.objects.create()
            hostel.h_name= request.POST['name']
            hostel.h_user = HAdmin.objects.get(id = request.session['login'])
            hostel.h_email = request.POST['email']
            hostel.h_contact = request.POST['contact']
            hostel.h_city = request.POST['city']
            hostel.h_address = request.POST['address']
            hostel.h_fees = request.POST['fees']
            hostel.save()
            return render(request,'app/addhostel.html',{})
        # return redirect(reverse('addhostel'))
        return render(request,'app/addhostel.html',{})


def updatehostel(request):
    
    try:
        if not request.session['login']:
            return redirect(reverse('login'))
        if request.POST['hostelid']:
            # print(request.POST)
            hostel = Hostel.objects.get(id= request.POST['hostelid'])
            # print(hostel)
            if request.POST['action']=='delete':
                hostel.delete()
                # return render(request,'app/viewhostel.html',{})
                return redirect(reverse('viewhostels'))
            request.session['hostelid']=request.POST['hostelid']
            print("*********************************************")
            print(hostel.h_name)
            print(hostel.h_email)
            return render(request,'app/updatehostel.html',{'hostel':hostel})
    except KeyError:
        return redirect(reverse('viewhostels'))


def updatehosteldata(request):
    
    try:
        if request.session['login']:
            # print(request.POST)
                # form = HostelForm
                hostel = Hostel.objects.get(id=request.session['hostelid'])
                hostel.h_name= request.POST['name']
                # hostel.h_user = HAdmin.objects.get(id = request.session['login'])
                hostel.h_email = request.POST['email']
                hostel.h_contact = request.POST['contact']
                hostel.h_city = request.POST['city']
                hostel.h_address = request.POST['address']
                hostel.h_fees = request.POST['fees']
                hostel.save()
                # return render(request,'app/viewhostel.html',{})
                return redirect(reverse('viewhostels'))
    except KeyError:    
        return redirect(reverse('login'))

# def select(request):
#     if request.POST['save']:
#         updatehosteldata(request)
#     elif request.POST['hostelid']:
#         updatehostel(request)



def viewhostel(request):
    
    try:
        hostelsobj = Hostel.objects.filter(h_user = request.session['login'])
        print(hostelsobj)
        context={}  
        try:
            return render(request,'app/viewhostel.html',{ 'hostels':hostelsobj })
        except Exception as e:
            print(e)
            return redirect('addhostel')
    except KeyError:
        return redirect(reverse('login'))

def addroom(request):
    
    try:
        hostelsobj = Hostel.objects.filter(h_user = request.session['login'])
        print(hostelsobj)
        return render(request,'app/addroom.html',{ 'hostels':hostelsobj })
    except Exception as e:
            print(e)
            return redirect(reverse('addroom'))

def saveroom(request):
    
    room = Room.objects.create()
    room.room_no = request.POST['roomno']
    room.hostel = Hostel.objects.get(id=request.POST['hostel'])
    room.capacity = request.POST['capacity']
    room.save()
    rooms = Hostel.objects.filter(id=request.POST['hostel'])
    return redirect(reverse('addroom'))
    # return render(request,'app/viewrooms.html',{'rooms':rooms})

def selecthostel(request):
    
    try:
        hostelsobj = Hostel.objects.filter(h_user = request.session['login'])
        # print(hostelsobj)
        print("At views selecthostel function")
        return render(request,'app/viewrooms.html',{ 'hostels':hostelsobj })
    except Exception as e:
            print(e)
            return redirect(reverse('selecthostel'))
    #  return render(request,'app/viewrooms.html',{})
    # rooms += Room.objects.filter(Q(hostel=5)|Q(hostel=6))

def viewrooms(request):
    
    try:
        print("views viewrooms function")
        hostelsobj = Hostel.objects.filter(h_user = request.session['login'])
        request.session['selectedhostel'] = request.POST['hostel']
        
        # print(request.session['selectedhostel'])
        if request.POST['hostel']:
            rooms = Room.objects.filter(hostel = request.POST['hostel'])
            print(rooms)
        else:
            rooms = Room.objects.filter(hostel=Hostel.objects.get(h_user=request.session['login']))
        # if request.POST['action']=="Delete":
        #     room = Room.objects.get(id=request.POST['roomid'])
        #     print('room is going to delete')
        #     room.delete()
        #     print('room deleted')
        return render(request,'app/deleteroom.html',{ 'rooms':rooms,'hostels':hostelsobj })
    except Exception as e:
        print("viewrooms functions exception")
        print(e)
        rooms = Room.objects.filter(hostel = request.POST['hostel'])
        return redirect(reverse('addhostel'))


def deleteroom(request):
    
    try:    
        print("deleterroom function")
        if request.POST['roomid']:
            print('post found')
            room = Room.objects.get(id=request.POST['roomid'])
            print('record found')
            room.delete()
            print('deleted')
            print(request.session['selectedhostel'])
            # if request.session['selectedhosted']:
            print("deleteroom if condition")
            rooms = Room.objects.filter(hostel = request.session['selectedhostel'])
            print(rooms)
            # return redirect(reverse('viewrooms'))
            # return render(request,'app/viewrooms.html',{})
            return render(request,'app/deleteroom.html',{'rooms':rooms})
        else:
            print("deleteroom functions else condition")
            if request.POST['hostel']:
                rooms = Room.objects.filter(hostel = request.POST['hostel'])
                print(rooms)
            else:
                rooms = Room.objects.filter(hostel=Hostel.objects.get(h_user=request.session['login']))
            return render(request,'app/deleteroom.html',{ 'rooms':rooms})
    except KeyError:
        return redirect(reverse('selecthostel'))

def selectforall(request):
    
    try:
        if not request.session['login']:
            return redirect(reverse('login'))
        hostelsobj = Hostel.objects.filter(h_user = request.session['login'])
        request.session['selectedhostel'] = request.POST['hostel']
        print("Hostel selected...")
        # print(hostelsobj)
        print("At views select function")
        return render(request,'app/selecthostel.html',{ 'hostels':hostelsobj })
    except Exception as e:
            print(e)    
            # return redirect(reverse('selectforall'))
            return render(request,'app/selecthostel.html',{ 'hostels':hostelsobj })


def addfacility_form(request):
    
    hostel = Hostel.objects.get(id=request.session['selectedhostel'])
    return render(request,'app/addfacility.html',{'hostel':hostel})


def addfacility(request):
    
    try:
        print("add facility function....")
        facility = Facility.objects.create(hostel=Hostel.objects.get(id=request.POST['hostel']))
        facility.hostel= Hostel.objects.get(id=request.POST['hostel'])
        facility.f_name=request.POST['fname']
        facility.f_description=request.POST['fdesc']
        facility.save()
        print("Object saved to Model")
        return redirect(reverse('addfacilityform'))
    except KeyError:
        return redirect(reverse('selectforall'))




def viewfacilities(request):
    
    try:
        facilities = Facility.objects.filter(hostel = request.session['selectedhostel'])
        print(facilities)
        try:
            return render(request,'app/viewfacilities.html',{ 'facilities':facilities })
        except Exception as e:
            print(e)
            return redirect('selectforall')
    except KeyError:
        return redirect(reverse('login'))

def deletefacility(request):
    
    print("Deletefacility function called")
    facility = Facility.objects.get(id=request.POST['action'])
    facility.delete()
    print("Facility deleted....")
    return redirect(reverse('viewfacility'))
#write code to delete the facility

def viewstudents(request):
    
    students = Student.objects.filter(hostel = request.session['selectedhostel'])
    print("viewstudents function....")
    print(students)
    return render(request,'app/viewstudents.html',{'students':students})


def addstudent(request):
    
    rooms = Room.objects.filter(hostel=request.session['selectedhostel'])         
    return render(request,'app/addstudent.html',{'rooms':rooms})
        # return redirect(reverse('addhostel'))
    

def savestudent(request):
        if not request.session['islogin']:
            return redirect(reverse('login'))
        if not request.session['login']:
            return redirect(reverse('login'))
        if request.POST:
            print(request.POST)
            student = Student.objects.create() 
            student.name= request.POST['name']
            student.email=request.POST['email']
            student.contact=request.POST['contact']
            student.hostel=Hostel.objects.get(id=request.session['selectedhostel'])
            student.room=Room.objects.get(id=request.POST['room'])
            student.save()
            return render(request,'app/addstudent.html',{})
        # return redirect(reverse('addhostel'))
        return render(request,'app/addstudent.html',{})

def deletestudent(request):
    
    try:
        if not request.session['login']:
            return redirect(reverse('login'))
        if request.POST['studentid']:
            # print(request.POST)
            student = Student.objects.get(id= request.POST['studentid'])
            # print(hostel)
            if request.POST['action']=='delete':
                student.delete()
                # return render(request,'app/viewhostel.html',{})
                return redirect(reverse('viewstudents'))
            request.session['studentid']=request.POST['studentid']
            rooms = Room.objects.filter(hostel=request.session['selectedhostel'])
            print("*********************************************")
            print(student.name)
            print(student.email)
            return render(request,'app/updatestudent.html',{'student':student,'rooms':rooms})
    except KeyError:
        return redirect(reverse('viewstudents'))

def updatestudent(request):
    
    if not request.session['login']:
            return redirect(reverse('login'))
    if request.POST:
        print(request.POST)
        student = Student.objects.get(id=request.POST['studentid']) 
        student.name= request.POST['name']
        student.email=request.POST['email']
        student.contact=request.POST['contact']
        student.hostel=Hostel.objects.get(id=request.session['selectedhostel'])
        student.room=Room.objects.get(id=request.POST['room'])
        student.save()
        # return render(request,'app/addstudent.html',{})
        return redirect(reverse('viewstudents'))
        # return render(request,'app/addstudent.html',{})
