from django.urls import (path, include,)
from django.contrib import admin
from students import views, class_views, mixin_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students-viewsets', mixin_views.StudentViewSet)

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
    path('students-class/', class_views.StudentList.as_view()),
    path('students-class/<int:pk>', class_views.StudentDetail.as_view()),
    path('students-mix/', mixin_views.StudentList.as_view()),
    path('students-mix/<int:pk>', mixin_views.StudentDetail.as_view()),
    path('', include(router.urls))
]

