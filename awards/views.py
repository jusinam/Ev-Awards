from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.

