from django.shortcuts import render
from . models import Car, Order, Service

# Create your views here.

def index(request):
    services_count = Service.objects.all().count()
    orders_completed = Order.objects.filter(status__exact=2).count()
    cars_count = Car.objects.all().count()

    context = {
        "services_count": services_count,
        "orders_completed": orders_completed,
        "cars_count": cars_count
    }
    return render(request, 'car_service/index.html', context)
