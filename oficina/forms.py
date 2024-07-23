from .models import Car, Mechanical, Service, Outflow
from django import forms


class MechanicalForm(forms.ModelForm):

    class Meta:
        model = Mechanical
        fields = ['nome']
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'})}


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['car_model']
        widgets = {
            'car_model': forms.TextInput(attrs={'class': 'form-control'})
        }


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            'responsible', 'car', 'service', 'service_price', 'license_plate',

        ]

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'service':
                field.widget.attrs['rows'] = 3


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = [
            'outflow', 'price',
        ]

    def __init__(self, *args, **kwargs):
        super(OutflowForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'service':
                field.widget.attrs['rows'] = 3
