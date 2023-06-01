from django.shortcuts import render,  get_object_or_404
from . models import Car, Order, Service
from django.views.generic import ListView
from django.core.paginator import Paginator


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

def car_list(request):
    paginator = Paginator(Car.objects.all(), 5)
    car_list = paginator.get_page(request.GET.get("page"))
    return render(request, 'car_service/car_list.html', {'cars': car_list})

def car_detail(request, pk: int):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_service/car_detail.html', {'car': car})

def order_detail(request, pk: int):
    order = get_object_or_404(Order, pk=pk)
    total_price = sum(entry.price for entry in order.order_entries.all())

    return render(request, 'car_service/order_detail.html', {'order': order, 'total_price': total_price})


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 3
    template_name = 'car_service/order_list.html'

    # def get_queryset(self):
    #     return super().get_queryset().prefetch_related('order_entries').annotate(total_price=Sum('order_entries__price'))