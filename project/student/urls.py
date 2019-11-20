from django.urls import path
from .views import *

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path(r'api/students/', ListStudentsView.as_view(), name="students_all"),

    path(r'api/details/<int:pk>',DetailStudentView.as_view(),name='student_detail'),

    path(r'api/create_student/',StudentCreateApiView.as_view(),name='student_create'),
    
    path(r'api/delete_student/<int:pk>',StudentDeleteApiView.as_view(),name='student_delete'),
    
    path(r'home/',index,name='home'),


    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
