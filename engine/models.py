from django.db import models

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
