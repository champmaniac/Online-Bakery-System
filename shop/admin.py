from django.contrib import admin
from .models import Contact,Inventory,Sale,Report
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Contact)
admin.site.register(Sale)
admin.site.register(Report)

