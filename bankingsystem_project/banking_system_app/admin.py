from django.contrib import admin

# Register your models here.
from banking_system_app.models import customers,history
admin.site.register(customers)
admin.site.register(history)