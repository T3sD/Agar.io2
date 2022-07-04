from django.shortcuts import render
from django.http import HttpResponse


def open(request):
    return render(request,'agar.html')
