from django.db import models

# Create your models here.


class setting(models.Model):
    param_def = models.BooleanField(blank=True, default=False,)
    schedule = models.CharField(max_length=50)
    exptype = models.BooleanField(blank=True, default=False,)
    export = models.CharField(max_length=50)
    uname = models.CharField(max_length=50, null=True)

    class Meta:
        db_table: 'setting'


class parameter(models.Model):
    param = models.CharField(max_length=100)
    desc = models.TextField()

    class Meta:
        db_table: 'parameter'
