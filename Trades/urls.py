from django.urls import path
from . import views

urlpatterns = [
    #ex: /Trades/
    path('', views.index, name='index'),
    #ex: /Trades/1/
    path('<int:OptionContract_id>/', views.detail, name='detail'),
]
