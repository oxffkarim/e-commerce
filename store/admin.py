from django.contrib import admin

# Register your models here.
from .models import category,customer,product,order
admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
