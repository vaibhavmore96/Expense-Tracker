from django.db import models
#from django.contrib.auth.models.import User
from django.utils.timezone import now
#from .models import Expense

# Create your models here.

class Expense(models.Model):
    Category = models.CharField(max_length=200)
    Items = models.CharField(max_length=300)
    Date = models.DateField(default=now)
    Amount = models.IntegerField(default=0)

    def __str__(self):
        return self.Items

    class Meta:
       ordering: ['-date']
