from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *



def index(request):
	return render(request, 'base/base.html')