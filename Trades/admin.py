from django.contrib import admin

from .models import OptionTrade, OptionContract

admin.site.register(OptionContract)
admin.site.register(OptionTrade)
