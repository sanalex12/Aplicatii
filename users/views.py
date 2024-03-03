from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from recipes.models import Recipe
from django.contrib import messages  

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()



def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'users/home.html', {'recipes': recipes})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if password1 and password2 and password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html', {'form': form})

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Username or email already exists.')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            messages.error(request, 'Username or password is incorrect.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
  logout(request)
  return redirect('login') 

def profile(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'recipes': recipes})

class RegisterViewSet(viewsets.ViewSet):
    
    @staticmethod
    def create(request):
 
        register_serializer = RegisterSerializer(data=request.POST)
        if register_serializer.is_valid():
            register_serializer.create(register_serializer.validated_data)
            
            
            content = {
                "message": "User created successfully",
            }
            return Response(content,status=200)
        return Response(register_serializer.errors,status=400)
    
    
    @staticmethod
    def list(request):
        all_users = AuthUserModel.objects.all()
        register_serializer = RegisterSerializer(all_users, many=True)
        content = {
            "users": register_serializer.data
        }
        return Response(content, status=200)