from django.db import models

# Create your models here.
class modes(models.Model):
    name = models.CharField(max_length=50)

class odPairs(models.Model):
    origin = models.CharField(max_length=25, db_index=True)
    destination = models.CharField(max_length=25, db_index=True)
    mode = models.ForeignKey('modes')
    ttime = models.FloatField(db_index=True)
    tdist = models.FloatField(db_index=True)