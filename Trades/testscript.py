from models import OptionContract


Test = OptionContract(stock="NFLX", k_open_date="2018-10-16",
    k_expiration_date="2018-11-19", directional_bias="Bullish")

Test.save()

OptionContract.objects.all()
Test.stock
