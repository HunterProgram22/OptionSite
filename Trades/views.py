from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Option Trade History listed here.")
