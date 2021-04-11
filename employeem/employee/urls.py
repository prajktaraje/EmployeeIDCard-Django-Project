from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.lhome,name='lhome'),
    path('showinfo/',views.showinfo,name='showinfo'),
    # path('download/',views.download,name='download'),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
     
]
