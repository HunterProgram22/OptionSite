from django.urls import path
from .views import Manage

urlpatterns = [
    #ex: /Trades/
    #path('', views.index, name='index'),
    #ex: /Trades/1/
    #path('<int:OptionContract_id>/', views.detail, name='detail'),
    path('manage.html', Manage.as_view(), name='TradesManage'),
    ]
