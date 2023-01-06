from django.db import models
from django.contrib.auth.models import User
from django.forms import PasswordInput


class Hostel(models.Model):
    h_name = models.CharField(max_length=100,verbose_name="Hostel Name")
    h_user = models.ForeignKey(User,verbose_name="Admin",on_delete=models.SET_NULL,null=True)         #hostel admin
    h_email = models.EmailField(max_length=100,verbose_name="Hostel Email")
    h_contact = models.CharField(max_length=100,verbose_name="Hostel Contact")
    h_city = models.CharField(max_length=30,verbose_name="City",null=True)
    h_address = models.TextField(max_length=100,verbose_name="Hostel Address")
    h_fees = models.IntegerField(null=True,verbose_name="Hostel Fees")
    h_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.h_name

class Facility(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE,verbose_name="Hostel")
    f_name = models.CharField(max_length=100,null=True,verbose_name="Hostel Facilities")
    f_description = models.CharField(max_length=200)

class Image(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
    file = models.CharField(max_length=200)
    
class Room(models.Model):
    room_no = models.CharField(max_length=30)
    hostel = models.ForeignKey(Hostel,on_delete=models.SET_NULL,null=True)
    capacity = models.CharField(max_length=30,null=True)
    #add field available space

    def __str__(self):
        # return str(self.hostel)+str(self.room_no)
        return str(self.room_no)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=30)
    hostel = models.ForeignKey(Hostel,on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null = True)
