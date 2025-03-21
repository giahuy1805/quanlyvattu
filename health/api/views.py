from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Patient
from .serializers import UserSerializer, PatientSerializer
from .forms import SignUpForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# ...existing code...

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin:index')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng hoặc bạn không có quyền truy cập.')
    return render(request, 'api/adminlogin.html')

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def home(request):
    return render(request, 'api/home.html')

def about(request):
    return render(request, 'api/about.html')

def login(request):
    return render(request, 'api/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'api/sign.html', {'form': form})