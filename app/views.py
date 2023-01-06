from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request,"app/login.html")

def home(request):
   return render(request, 'app/home.html', {})

def register(request):
    # form = UserCreationForm()
    form = CreateUserForm()
    form.fields['username'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Username'}
    form.fields['email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
    form.fields['first_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'First Name'}
    form.fields['last_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Last Name'}
    form.fields['password1'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Password'}
    form.fields['password2'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Confirm Password'}
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        form.fields['username'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Username'}
        form.fields['email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
        form.fields['first_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'First Name'}
        form.fields['last_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Last Name'}
        form.fields['password1'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Password'}
        form.fields['password2'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Confirm Password'}
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # to send the success messages to the login page
            messages.success(request,f'You can now login with username \'{user}\'')
            return redirect('login')
    context = {'form':form}
    return render(request,'app/register.html',context)
    

def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username, password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"Incorrect username or password!")
    context={}
    return render (request,'app/login.html',context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'app/dashboard.html', {})




def addhostel(request):
    form = HostelForm()
    form.fields['h_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Hostel Name'}
    form.fields['h_email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
    form.fields['h_contact'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Contact Number'}
    form.fields['h_address'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Address'}
    form.fields['h_city'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'City'}
    form.fields['h_fees'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Fees'}
    if request.POST:  
        form = HostelForm(request.POST)
        form.fields['h_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Hostel Name'}
        form.fields['h_email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
        form.fields['h_contact'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Contact Number'}
        form.fields['h_address'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Address'}
        form.fields['h_city'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'City'}
        form.fields['h_fees'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Fees'}
        if form.is_valid():
            hostel = Hostel.objects.create()
            hostel.h_name = form.cleaned_data['h_name']
            hostel.h_email = form.cleaned_data['h_email']
            hostel.h_contact = form.cleaned_data['h_contact']
            hostel.h_address = form.cleaned_data['h_address']
            hostel.h_city = form.cleaned_data['h_city']
            hostel.h_fees = form.cleaned_data['h_fees']
            hostel.h_user = request.user
            hostel.save()
            messages.info(request,"Hostel data is saved!")
        return render(request,'app/addhostel.html',{'form':form})
    return render(request,'app/addhostel.html',{'form':form})

@login_required(login_url='login')
def deletehostel(request,pk):
    if request.method=="POST":
        hostel = Hostel.objects.get(id=pk)
        hostel.delete()
        return redirect(reverse('viewhostels'))


@login_required(login_url='login')
def updatehostel(request,pk):
    hostel = Hostel.objects.get(id= pk)
    print("this is hostel data: ",hostel.id)
    form = HostelForm(instance=hostel)
    form.fields['h_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Hostel Name'}
    form.fields['h_email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
    form.fields['h_contact'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Contact Number'}
    form.fields['h_address'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Address'}
    form.fields['h_city'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'City'}
    form.fields['h_fees'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Fees'}
    if request.method=='POST':
        form = HostelForm(request.POST,instance=hostel)
        form.fields['h_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Hostel Name'}
        form.fields['h_email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
        form.fields['h_contact'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Contact Number'}
        form.fields['h_address'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Address'}
        form.fields['h_city'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'City'}
        form.fields['h_fees'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Fees'}
        if form.is_valid():
            hostel.h_name = form.cleaned_data['h_name']
            hostel.h_email = form.cleaned_data['h_email']
            hostel.h_contact = form.cleaned_data['h_contact']
            hostel.h_address = form.cleaned_data['h_address']
            hostel.h_city = form.cleaned_data['h_city']
            hostel.h_fees = form.cleaned_data['h_fees']
            hostel.save()
            messages.info(request,"Hostel data is saved!")
            return render(request,'app/updatehostel.html',{'form':form})
    return render(request,'app/updatehostel.html',{'form':form})


def updatehosteldata(request,pk):
    hostel = Hostel.objects.get(id=pk)
    form = HostelForm(hostel)
    if request.method=='POST':
        form = HostelForm(request.POST)
        form.fields['h_name'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Hostel Name'}
        form.fields['h_email'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Email Id'}
        form.fields['h_contact'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Contact Number'}
        form.fields['h_address'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Address'}
        form.fields['h_city'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'City'}
        form.fields['h_fees'].widget.attrs = {'class':'w3-input w3-border w3-round', 'placeholder':'Fees'}
        if form.is_valid():
            hostel.h_name = form.cleaned_data['h_name']
            hostel.h_email = form.cleaned_data['h_email']
            hostel.h_contact = form.cleaned_data['h_contact']
            hostel.h_address = form.cleaned_data['h_address']
            hostel.h_city = form.cleaned_data['h_city']
            hostel.h_fees = form.cleaned_data['h_fees']
            hostel.save()
            messages.info(request,"Hostel data is updated!")
            return render(f'app/viewhostels/{hostel.id}/')
    return render(f'app/viewhostels/{hostel.id}/')

@login_required(login_url='login')
def viewhostel(request):
    hostelsobj = Hostel.objects.filter(h_user = request.user)
    print(hostelsobj)
    context={'hostels':hostelsobj}  
    return render(request,'app/viewhostel.html',context)
  

@login_required(login_url='login')
def addroom(request):
    hostelsobj = Hostel.objects.filter(h_user = request.user)
    return render(request,'app/addroom.html',{ 'hostels':hostelsobj })

@login_required(login_url='login')
def saveroom(request):
    
    room = Room.objects.create()
    room.room_no = request.POST['roomno']
    room.hostel = Hostel.objects.get(id=request.POST['hostel'])
    room.capacity = request.POST['capacity']
    room.save()
    messages.info(request,"Room data added successfully!")
    return redirect(reverse('addroom'))


@login_required(login_url='login')
def selecthostel(request):
    hostelsobj = Hostel.objects.filter(h_user =request.user)
    context={"hostels":hostelsobj,"rooms":None}
    if request.method=='POST':
        rooms = Room.objects.filter(hostel = request.POST.get('hostel',None))
        
        context={"hostels":hostelsobj,'rooms':rooms}
        if len(rooms)== 0:
            messages.info(request," NO rooms found for selected hostel!")
        else:
            messages.info(request,f"Selected Hostel is \'{rooms.first().hostel}\'")
        return render(request,'app/viewrooms.html',context=context)
    return render(request,'app/viewrooms.html',context=context)


@login_required(login_url='login')
def deleteroom(request):
    if request.method=='POST':
        room = Room.objects.get(id=request.POST.get('pk',None))
        room.delete()
        messages.info(request,"Room deleted successfully!")
        return redirect(reverse('selecthostel'))
    messages.info(request,"Something went wrong!")
    return redirect(reverse('selecthostel'))


@login_required(login_url='login')    
def addfacility_form(request):
    hostels = Hostel.objects.filter(h_user=request.user)
    context={'hostels':hostels,'facilities':None}
    if request.method=='POST':
        facilities = Facility.objects.filter(hostel=request.POST.get('hostel',None))
        facility = Facility.objects.create(hostel=Hostel.objects.get(id=request.POST['hostel']))
        facility.hostel= Hostel.objects.get(id=request.POST['hostel'])
        facility.f_name=request.POST['fname']
        facility.f_description=request.POST['fdesc']
        facility.save()
        print('this is hostel data from the post method :',request.POST.get('hostel'))
        context = {'hostels':hostels,'facilities':facilities}
    return render(request,'app/addfacility.html',context=context)

@login_required(login_url='login')
def addfacility(request):
    facility = Facility.objects.create(hostel=Hostel.objects.get(id=request.POST['hostel']))
    facility.hostel= Hostel.objects.get(id=request.POST['hostel'])
    facility.f_name=request.POST['fname']
    facility.f_description=request.POST['fdesc']
    facility.save()
    return redirect(reverse('addfacilityform'))



@login_required(login_url='login')
def viewfacilities(request):
    hostelsobj = Hostel.objects.filter(h_user =request.user)
    context={"hostels":hostelsobj,"facilities":None}
    if request.method=='POST':
        facilities = Facility.objects.filter(hostel = request.POST.get('hostel',None))
        
        context={"hostels":hostelsobj,'facilities':facilities}
        if len(facilities)== 0:
            messages.info(request," NO rooms found for selected hostel!")
        else:
            messages.info(request,f"Selected Hostel is \'{facilities.first().hostel}\'")
        return render(request,'app/viewfacilities.html',context=context)
    return render(request,'app/viewfacilities.html',context=context)


@login_required(login_url='login')
def deletefacility(request):
    
    print("Deletefacility function called")
    facility = Facility.objects.get(id=request.POST['pk'])
    facility.delete()
    return redirect(reverse('viewfacility'))


@login_required(login_url='login')
def viewstudents(request):
    hostels = Hostel.objects.filter(h_user = request.user)
    context={'hostels':hostels,'students':None}
    if request.method=='POST':
        students = Student.objects.filter(hostel = request.POST['hostel'])
        context = {'hostels':hostels,'students':students}
        return render(request,'app/viewstudents.html',context=context)
    return render(request,'app/viewstudents.html',context=context)
    



@login_required(login_url='login')
def addstudent(request):
    hostels = Hostel.objects.filter(h_user = request.user)
    rooms = Room.objects.filter(hostel=request.POST.get(('hostel')))
    return render(request,'app/addstudent.html',{'rooms':rooms,'hostels':hostels})

@login_required(login_url='login')
def savestudent(request):
        if request.POST:
            print(request.POST)
            hostel=Hostel.objects.get(id=request.POST.get('hostel'))
            student = Student.objects.create()
            name = request.POST.get('name',None)
            email = request.POST.get("email",None)
            contact = request.POST.get("contact",None)
            room = request.POST.get("room",None)
            if name is None or name =="":
                messages.error(request,"Name can not be empty!")
                return render(request,'app/addstudent.html')
            #add validations here
            student.name= name
            student.email=request.POST['email']
            student.contact=request.POST['contact']
            student.hostel = hostel
            student.room=Room.objects.get(hostel=hostel,id=room)
            student.save()
            return render(request,'app/addstudent.html',{})
        return render(request,'app/addstudent.html',{})

@login_required(login_url='login')
def deletestudent(request):
    if request.POST['pk']:
        student = Student.objects.get(id= request.POST['pk'])
        student.delete()
        return redirect(reverse('viewstudents'))
    return redirect(reverse('viewstudents'))
            

@login_required(login_url='login')
def updatestudent(request,pk):    
    if request.POST:
        print(request.POST)
        student = Student.objects.get(id=request.POST['studentid']) 
        student.name= request.POST['name']
        student.email=request.POST['email']
        student.contact=request.POST['contact']
        student.hostel=Hostel.objects.get(id=request.session['selectedhostel'])
        student.room=Room.objects.get(id=request.POST['room'])
        student.save()
        return redirect(reverse('viewstudents'))
