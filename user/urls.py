from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('profile', views.profile,name='profile'),
    path('createaccount/', views.register,
         name='create_account'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logout1,name='logout1'),
    path('changenumber/', views.change_number, name='change_number'),
    path('changeemail/', views.change_email, name='change_email'),
    path('login2/', views.login2, name='login2'),
    path('login3/', views.login3, name='login3')
]
