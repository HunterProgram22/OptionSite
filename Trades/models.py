from django.db import models

class OptionContract(models.Model):
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"
    DIRECTIONAL_BIAS_CHOICES = (
        (BULLISH, "Bullish"),
        (BEARISH, "Bearish"),
        (NEUTRAL, "Neutral"),
    )

    stock = models.CharField(max_length=10)
    k_open_date = models.DateField('Date Opened')
    k_expiration_date = models.DateField('Expiration Date')
    directional_bias = models.CharField(
        max_length=10,
        choices = DIRECTIONAL_BIAS_CHOICES,
        default = BULLISH,
        )

    def __str__(self):
        return self.stock + str(self.k_expiration_date)
