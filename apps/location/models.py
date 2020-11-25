from django.db import models

class Address(models.Model):

    digital_address = models.CharField(blank=True, max_length=15)
    postal_address = models.CharField(blank=True, max_length=30)
    house_number = models.CharField(blank=True, max_length=15)
    town = models.CharField(max_length=20)

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "address"

    def __str__(self):
        return self.digital_address
