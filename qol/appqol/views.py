from django.shortcuts import render, redirect
import requests
import json

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'hospital.html')

def main_home(request):
    return render(request, 'main.html')

def hospital_add(request):
    return render(request, 'hospital_add.html')

def hos_name(request):
    return render(request, 'show_hos.html')

   
# def hos_search(request):
#     if request.method == "POST":
#         hospital = request.POST['searched']
#         return render(request, 'hospital_add.html', {'hospital':hospital})