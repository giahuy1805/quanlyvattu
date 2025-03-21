from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sign/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('adminlogin/', views.admin_login, name='admin_login'),
    path('patients/', views.PatientListCreate.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroy.as_view(), name='patient-retrieve-update-destroy'),
]