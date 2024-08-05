from django.urls import (path, include,)
from django.contrib import admin
from students import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
]

