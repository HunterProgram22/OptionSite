from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Option Trade History listed here.")

def detail(request, OptionContract_id):
    return HttpResponse("You're looking at trade %s." % OptionContract_id)
