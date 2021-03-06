from django.db import models

from django_chinook.core.models import BaseModel


class Employee(BaseModel):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=20)
    reports_to = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE)
    birth_date = models.DateTimeField()
    hire_date = models.DateTimeField()
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    class Meta:
        ordering = ('last_name',)
