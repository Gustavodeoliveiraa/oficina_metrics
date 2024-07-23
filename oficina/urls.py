from django.urls import path
from .views import (
    MechanicalCreateView, MechanicalListView, MechanicalDeleteView,
    MechanicalUpdateView
)
from .views import (
    CarCreateView, CarListView, CarDeleteView,
    CarUpdateView
)
from .views import (
    ServiceCreateView, ServiceListView, ServiceDeleteView,
    ServiceUpdateView
)

from .views import (
    OutflowCreateView, OutflowDeleteView, OutflowListView, OutflowUpdateView
)

urlpatterns = [
    path(
        'mechanical/create', MechanicalCreateView.as_view(),
        name='create_mechanical'
    ),
    path(
        'mechanical/list', MechanicalListView.as_view(),
        name='list_mechanical'
    ),
    path(
        'delete/mechanical/<int:pk>', MechanicalDeleteView.as_view(),
        name='delete_mechanical'
    ),
    path(
        'update/mechanical/<int:pk>', MechanicalUpdateView.as_view(),
        name='update_mechanical'
    ),
    #   --------------------------------------------------------------

    path(
        'car/create', CarCreateView.as_view(),
        name='create_car'
    ),
    path(
        'car/list', CarListView.as_view(),
        name='list_car'
    ),
    path(
        'car/delete/<int:pk>', CarDeleteView.as_view(),
        name='delete_car'
    ),
    path(
        'car/update/<int:pk>', CarUpdateView.as_view(),
        name='update_car'
    ),
    #   --------------------------------------------------------------
    path(
        'service/create', ServiceCreateView.as_view(),
        name='create_service'
    ),
    path(
        '', ServiceListView.as_view(),
        name='list_service'
    ),
    path(
        'service/delete/<int:pk>', ServiceDeleteView.as_view(),
        name='delete_service'
    ),
    path(
        'service/update/<int:pk>', ServiceUpdateView.as_view(),
        name='update_service'
    ),

    #   --------------------------------------------------------------

    path(
        'outflow/create', OutflowCreateView.as_view(),
        name='create_outflow'
    ),
    path(
        'outflow', OutflowListView.as_view(),
        name='list_outflow'
    ),
    path(
        'outflow/delete/<int:pk>', OutflowDeleteView.as_view(),
        name='delete_outflow'
    ),
    path(
        'outflow/update/<int:pk>', OutflowUpdateView.as_view(),
        name='update_outflow'
    ),
]
