from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.email_form, name='about'),
  path('portfolio/', views.portfolio, name='portfolio'),
]