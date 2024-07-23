from django.db import models


class Mechanical(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome


class Car(models.Model):
    car_model = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.car_model


class Service(models.Model):
    responsible = models.ForeignKey(
        Mechanical, on_delete=models.PROTECT, blank=False, null=False
    )
    car = models.ForeignKey(
        Car, on_delete=models.PROTECT, max_length=255, null=False, blank=False
    )
    service = models.TextField(max_length=255, null=False, blank=False)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    license_plate = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)


class Outflow(models.Model):
    outflow = models.TextField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
