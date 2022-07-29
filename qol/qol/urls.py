from django.contrib import admin
from django.urls import path
from appqol import views
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('search/', views.search, name='search'),
    path('main_home/', views.main_home, name='main_home'),
    path('hospital_add/', views.hospital_add, name='hospital_add'),
    path('hos_name/', views.hos_name, name='hos_name')
]
