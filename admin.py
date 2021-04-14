from django.contrib import admin
from .models import Expense

#Register your models here.
#class ExpenseDetails(admin.ModelAdmin):
   # fields = ('Category','Items','Amount','Date')

   # list_display = ('Category','Items','Amount','Date')
admin.site.register(Expense)
