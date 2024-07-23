from typing import Dict, List, Union
from django.utils import timezone
from oficina.models import Service, Outflow
from django.db.models import Sum


def get_daily_sales_date() -> Dict[str, Union[str, List]]:
    """
    return a dictionary with the dates of last 7 days and the total sales
    for each date

    Returns:
        dict: A dict with the following keys:
            - 'dates': List of strings representing the dates of last 7 days.
            - 'values': List of floats representing the total of seles for each
                corresponding date.
    """
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(10, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Service.objects.filter(
                created_at=date
        ).aggregate(
                total_sales=(Sum('service_price'))
        )['total_sales'] or 0

        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values
    )


def get_daily_sales_quantity_data() -> Dict[str, Union[List[str], List[int]]]:
    """
    return a dictionary with the quantities of sales for each day in the last 7
    days

    Returns:
        dict: A dict with the following keys:
            -'dates': List of strings representing the dates of the last 7 days
            -'quantities': List of integer that representing the number of
            sales per day
    """
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(10, -1, -1)]
    quantities = list()

    for date in dates:
        daily_sales = Service.objects.filter(
            created_at=date
        ).count()
        quantities.append(daily_sales)

    return dict(
        dates=dates,
        values=quantities
    )


def get_total_sales_price():
    total_sales = Service.objects.aggregate(
        total_sales=Sum('service_price')
    )['total_sales'] or 0

    return float(total_sales)


def get_outflow_price():
    total_sales = Outflow.objects.aggregate(
        total_sales=Sum('price')
    )['total_sales'] or 0

    return float(total_sales)