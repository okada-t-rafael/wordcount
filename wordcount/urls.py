from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('count/', views.count_view, name='count'),
    path('about/', views.about_view, name='about')
]
