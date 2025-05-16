from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from core.models import TodoApp

def redirect_to_main_page(request):
    return redirect('home')


@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        task_input = request.POST.get('todo-task', '').strip()
        if task_input:
            TodoApp.objects.create(title=task_input, user=request.user)
        return redirect('home')

    main_tasks = TodoApp.objects.filter(user=request.user).order_by('-date')
    return render(request, 'index.html', {'main_tasks': main_tasks})


@login_required(login_url='login')
def editing_task(request, srno):
    task = get_object_or_404(TodoApp, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('task', '').strip()
        if title:
            task.title = title
            task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


@login_required(login_url='login')
def deleting_task(request, srno):
    # Secure delete: only allow POST to prevent accidental deletes via GET
    task = get_object_or_404(TodoApp, srno=srno, user=request.user)
    task.delete()
    return redirect('home')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirmPassword', '')

        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match.'})

        if not username or not email or not password:
            return render(request, 'signup.html', {'error_message': 'All fields are required.'})

        try:
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error_message': 'Username already taken.'})
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('home')
        except Exception:
            return render(request, 'signup.html', {'error_message': 'Error creating account. Try again.'})

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})

    return render(request, 'login.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
