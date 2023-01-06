from django.contrib import admin
from .models import *
# Register your models here.


class HostelAdmin(admin.ModelAdmin):
    list_display = ('id','h_name','h_user','h_email','h_contact','h_city','h_address','h_fees','h_registered')
admin.site.register(Hostel,HostelAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=('id','room_no','hostel')
admin.site.register(Room,RoomAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','contact','hostel','room')
admin.site.register(Student,StudentAdmin)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('id','hostel','f_name','f_description')
admin.site.register(Facility,FacilityAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display=('id','hostel','file')
admin.site.register(Image,ImageAdmin)