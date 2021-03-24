from django.db import models
from django.utils.timezone import now
# Create your models here.


class Source(models.Model):
    HRD = 'HRD'
    MANAGER = 'Manager'
    STAFF = 'Staff'
    DIRECTOR = 'Director'
    opt = [
        (HRD, 'HRD'),
        (MANAGER, 'Manager'),
        (STAFF, 'Staff'),
        (DIRECTOR, 'Director'),
    ]

    role = models.CharField(
        max_length=20,
        choices=opt,
        default=HRD,
    )

    source = models.CharField(max_length=100)
    auth = models.BooleanField(
        blank=True,
        default=False,
    )

    class Meta:
        db_table = 'source'


class results(models.Model):
    number = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=200, blank=True)
    loc = models.CharField(max_length=200, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    likelihood = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'results'


class breaker(models.Model):
    username = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=10, blank=True)
    time = models.DateTimeField(default=now, blank=True)

    class Meta:
        db_table = 'breaker'
