from django.shortcuts import render

def landing(request):
    return render(request, 'main/landing.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def main(request):
    return render(request, 'main/main.html')