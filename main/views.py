from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Course

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


def landing(request):
    return render(request, 'main/landing.html')

def main(request):
    courses = Course.objects.filter(users=request.user)
    print(courses)
    context = {
        'courses': courses, 
    }
    return render(request, 'main/main.html', context=context) 


# Sign Up View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'