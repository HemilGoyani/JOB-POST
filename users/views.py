# users/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, CustomUserUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # or wherever you want
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.name}!")
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def update_user(request, pk):
    employee = User.objects.get(id=pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = CustomUserUpdateForm(instance=employee)
    return render(request, 'update.html', {'form':form})

@login_required
def delete_user(request, pk):
    employee = User.objects.get(id= pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')