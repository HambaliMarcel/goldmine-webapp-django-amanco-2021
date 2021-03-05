from django.db import models

# Create your models here.


class Source(models.Model):
    source = models.CharField(max_length=100)
    auth = models.CharField(max_length=5)
    role = models.CharField(max_length=20)

    class Meta:
        db_table = 'source'
