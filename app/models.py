from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tovar(models.Model):
    opis = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=50)
    skidka = models.FloatField(default=1)
    vkorzine = models.BooleanField(default=False)

    def __str__(self):
        return self.opis

class Korzina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.tovar.price * self.tovar.skidka

class Zakaznew(models.Model):
    adres = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=12)
    total = models.IntegerField()
    samzakaz = models.TextField()

class Izbran(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)