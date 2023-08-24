from django.contrib import admin
from .models import *

# Register your models here.
# class AttendanceAdmin(admin.ModelAdmin):
#     fields    = ('user', 'timestamp', 'action')

#     #list of fields to display in django admin
#     list_display = ['user', 'timestamp', 'action']


#     #if you want django admin to show the search bar, just add this line
#     # search_fields = ['name', 'slug']

#     #to define model data list ordering
#     # ordering = ('id','name')


admin.site.register(Registeration)
admin.site.register(Attendance)
