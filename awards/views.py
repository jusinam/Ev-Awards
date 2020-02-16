from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

# Create your views here.
def home(request): 

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created successfully')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})
