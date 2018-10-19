from django.db import models

# k is shorthand for contract

class OptionContract(models.Model):
    LONG_CALL = "Buy Call"
    LONG_PUT = "Buy Put"
    SHORT_CALL = "Sell Call"
    SHORT_PUT = "Sell Put"
    CONTRACT_TYPE_CHOICES = (
        (LONG_CALL, "Buy Call"),
        (LONG_PUT, "Buy Put"),
        (SHORT_CALL, "Sell Call"),
        (SHORT_PUT, "Sell Put"),
    )

    stock = models.CharField(max_length=10)
    option_price = models.DecimalField(max_digits=8, decimal_places=2)
    strike_price = models.DecimalField(max_digits=8, decimal_places=2)
    k_open_date = models.DateField('Date Opened')
    k_expiration_date = models.DateField('Expiration Date')
    option_type = models.CharField(
        max_length=10,
        choices = CONTRACT_TYPE_CHOICES,
        default = LONG_CALL
        )

    def __str__(self):
        return self.stock + str(self.k_expiration_date)

    def days_to_exp(self):
        return self.k_expiration_date - self.k_open_date


class OptionTrade(models.Model):
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"
    DIRECTIONAL_BIAS_CHOICES = (
        (BULLISH, "Bullish"),
        (BEARISH, "Bearish"),
        (NEUTRAL, "Neutral"),
    )

    directional_bias = models.CharField(
        max_length=10,
        choices = DIRECTIONAL_BIAS_CHOICES,
        default = BULLISH,
        )

    def __str__(self):
        return self.directional_bias
