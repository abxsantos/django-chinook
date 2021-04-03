from django.db import models

from django_chinook.core.models import BaseModel
from django_chinook.employee.models import Employee
from django_chinook.music.models import Track


class Customer(BaseModel):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, default=None, blank=True, null=True)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40, default=None, blank=True, null=True)
    country = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10, default=None, blank=True, null=True)
    phone = models.CharField(max_length=24, default=None, blank=True, null=True)
    fax = models.CharField(max_length=24, default=None, blank=True, null=True)
    email = models.CharField(max_length=60)
    support_rep = models.ForeignKey(Employee, models.PROTECT, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ('last_name',)


class Invoice(BaseModel):
    customer = models.ForeignKey(Customer, models.PROTECT)
    invoice_date = models.DateTimeField()
    billing_address = models.CharField(max_length=70)
    billing_city = models.CharField(max_length=40)
    billing_state = models.CharField(max_length=40, default=None, blank=True, null=True)
    billing_country = models.CharField(max_length=40)
    billing_postal_code = models.CharField(max_length=10, default=None, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)


class InvoiceLine(BaseModel):
    invoice = models.ForeignKey(Invoice, models.PROTECT)
    track = models.ForeignKey(Track, models.PROTECT)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()


class Playlist(BaseModel):
    play_list = models.CharField(max_length=60)
    customer = models.ManyToManyField(Customer)
    track = models.ManyToManyField(Track)

    def __str__(self):
        return self.play_list

    class Meta:
        ordering = ('play_list',)
