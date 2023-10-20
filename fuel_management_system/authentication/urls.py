from django.urls import path
from .views import *

urlpatterns = [
    path('register/',Registeration_view.as_view(), name = 'Register'),
    path('login/', Login_View.as_view(), name = 'Login'),
    path('users/', UserView.as_view(), name = 'users'),
    path('attendance/<str:action>/', Attendance_View.as_view(), name = 'Attendance'),
    path('attendance/', get_attendance, name = 'Attendance'),
    path('attendance_by_user/<int:id>/', list_of_attendance_by_id, name = 'Attendance_by_id'),

]