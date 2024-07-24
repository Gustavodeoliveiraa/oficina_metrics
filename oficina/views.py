from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Mechanical, Car, Service, Outflow
from .forms import MechanicalForm, CarForm, ServiceForm, OutflowForm
from django.urls import reverse_lazy
from .metrics import get_daily_sales_date, get_daily_sales_quantity_data, get_total_sales_price, get_outflow_price


class MechanicalCreateView(CreateView):
    model = Mechanical
    form_class = MechanicalForm
    template_name = 'components/mechanical/create_mechanical.html'
    success_url = reverse_lazy('list_mechanical')


class MechanicalListView(ListView):
    model = Mechanical
    context_object_name = 'mechanics'
    template_name = 'components/mechanical/list_mechanical.html'

    def get_queryset(self):
        name = self.request.GET.get('nome')
        queryset = super().get_queryset()

        if name:
            queryset = Mechanical.objects.filter(nome__icontains=name)

        return queryset


class MechanicalDeleteView(DeleteView):
    model = Mechanical
    template_name = 'components/mechanical/delete_mechanical.html'
    success_url = reverse_lazy('list_mechanical')


class MechanicalUpdateView(UpdateView):
    model = Mechanical
    form_class = MechanicalForm
    template_name = 'components/mechanical/update_mechanical.html'
    success_url = reverse_lazy('list_mechanical')

# -------------------------------------------------------------------


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'components/car/create_car.html'
    success_url = reverse_lazy('list_car')


class CarListView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'components/car/list_car.html'

    def get_queryset(self):
        name = self.request.GET.get('car_model')
        queryset = super().get_queryset()

        if name:
            queryset = Car.objects.filter(car_model__icontains=name)

        return queryset


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'components/car/delete_car.html'
    success_url = reverse_lazy('list_car')


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'components/car/update_car.html'
    success_url = reverse_lazy('list_car')

# -------------------------------------------------------------------


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'components/service/create_service.html'
    success_url = reverse_lazy('list_service')


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'components/service/list_service.html'

    def get_queryset(self):
        name = self.request.GET.get('car_model')
        queryset = super().get_queryset()

        if name:
            queryset = Service.objects.filter(car_model__icontains=name)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['daily_sales_date'] = get_daily_sales_date()
        context['daily_sales_quantity_date'] = get_daily_sales_quantity_data()
        context['total_sales'] = get_total_sales_price()
        context['total_cost'] = get_outflow_price()
        return context


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'components/service/delete_service.html'
    success_url = reverse_lazy('list_service')


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'components/service/update_service.html'
    success_url = reverse_lazy('list_service')

# -------------------------------------------------------------------


class OutflowCreateView(CreateView):
    model = Outflow
    form_class = OutflowForm
    template_name = 'components/outflow/create_outflow.html'
    success_url = reverse_lazy('list_outflow')


class OutflowListView(ListView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'components/outflow/list_outflow.html'


class OutflowDeleteView(DeleteView):
    model = Outflow
    template_name = 'components/outflow/delete_outflow.html'
    success_url = reverse_lazy('list_outflow')


class OutflowUpdateView(UpdateView):
    model = Outflow
    form_class = OutflowForm
    template_name = 'components/outflow/update_outflow.html'
    success_url = reverse_lazy('list_outflow')
