from django.contrib import admin
from . import models

class OrderAdmin(admin.ModelAdmin):
    list_display = ("car", "date", "price")


class CarAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "model", "vin", "client")
    list_filter = ("client", "model")
    search_fields = ("license_plate", "vin")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price")


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderEntry)
admin.site.register(models.Service, ServiceAdmin)
# OrderAdmin