from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import generics
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers as django_serializers
from django.forms import ValidationError
from django.forms.models import model_to_dict
from django.http import FileResponse, HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from notify.signals import notify
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.authtoken.models import Token
from .models import *
import ast
import random
import os
import time
import csv
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from core.models import ClassificationModel,RegressionModel,Dataset

from Classification.RandomForest import func1

from Regression.multipleregression import func2


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
   

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def list_classifier(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    cmodels = ClassificationModel.objects.all()
    variable= " "    
    
    context = {
        'cmodels': cmodels,
        'variable':variable
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'classifiers.html', context=context)


def list_regression(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
   
    # Generate counts of some of the main objects
    rmodels = RegressionModel.objects.all()
    variable= " "    
    
    
    context = {
        'rmodels': rmodels,
        'variable':variable
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'regression.html', context=context)

def landing(request):
    num_cmodels = ClassificationModel.objects.all().count()
    num_rmodels = RegressionModel.objects.all().count()
    
    num_tdatasets = Dataset.objects.all().count()
    

    context = {
        'num_cmodels': num_cmodels,
        'num_rmodels': num_rmodels,
        'num_tdatasets': num_tdatasets,
    }

    return render(request,'landing.html',context=context)

def analysis(request):
    return render(request,'analysis.html')

def Random_forests(request):
    cmodels = ClassificationModel.objects.all()
   
    variable = func1()
     
    context = {
        'cmodels': cmodels,
        'variable':variable
    }
    return render(request,"classifiers.html", context=context)



def multipleregression(request):
    rmodels = RegressionModel.objects.all()
   
    variable = func2()
     
    context = {
        'rmodels': rmodels,
        'variable':variable
    }
    return render(request,"regression.html", context=context)
