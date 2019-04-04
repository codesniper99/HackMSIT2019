from django.urls import path, re_path, include
from django.conf import settings

from rest_framework.authtoken import views as rf_auth_views
from rest_framework.documentation import include_docs_urls

from rest_framework import routers
import coreapi
from . import views


router = routers.DefaultRouter()

urlpatterns = [
     path('', views.index, name='index'),
     path('classifiers', views.list_classifier, name='classifiers'),
     path('regression', views.list_regression, name='regression'),
     path('landing',views.landing, name='landing'),
     path('analysis',views.analysis,name='analysis'),
     path('classifiers/randomf',views.Random_forests, name='randomf'),
     path('regression/multipleregression',views.multipleregression, name='multipleregression'),

]