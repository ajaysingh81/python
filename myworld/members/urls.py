from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    
    path('', views.temp, name = 'temp'), # instead of empty string you can right "temp/"
    path('members/',views.members, name = 'members'),
    path('members/details/<int:id>', views.details, name = 'members'),

]