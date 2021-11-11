from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_home, name='create_home'),
    path('monday', views.mond, name='mond'),
    path('tuesday', views.Tuesday, name='tued'),
    path('wednesday', views.Wednesday, name='wedn'),
    path('thursday', views.Thursday, name='thur'),
    path('friday', views.Friday, name='frid')


]
