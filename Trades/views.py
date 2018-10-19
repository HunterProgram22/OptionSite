from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import OptionContract, OptionTrade

class Manage(View):
    def get(self, request):
        return render(request, 'Trades/manage.html', {})




def index(request):
    all_trades = OptionTrade.objects.all()
    all_contracts = OptionContract.objects.all()
    context = {
        'all_trades': all_trades,
        'all_contracts': all_contracts,
        }
    return render(request, 'Trades/index.html', context)

def detail(request, OptionContract_id):
    return HttpResponse("You're looking at trade %s." % OptionContract_id)
