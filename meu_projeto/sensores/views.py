from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor, Leitura
from .forms import SensorForm, LeituraForm

def create_sensor(request):
    if request.method == "POST":
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sensors')
    else:
        form = SensorForm()
    return render(request, 'sensores/create_sensor.html', {'form': form})

def list_sensors(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensores/list_sensors.html', {'sensors': sensors})

def update_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    if request.method == "POST":
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('list_sensors')
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'sensores/update_sensor.html', {'form': form})

def delete_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    sensor.delete()
    return redirect('list_sensors')

def create_leitura(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    if request.method == "POST":
        form = LeituraForm(request.POST)
        if form.is_valid():
            leitura = form.save(commit=False)
            leitura.sensor = sensor
            leitura.save()
            return redirect('list_sensors')
    else:
        form = LeituraForm()
    return render(request, 'sensores/create_leitura.html', {'form': form, 'sensor': sensor})

def list_leituras(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    leituras = Leitura.objects.filter(sensor=sensor)
    return render(request, 'sensores/list_leituras.html', {'sensor': sensor, 'leituras': leituras})


def home(request):
    return render(request, 'sensores/home.html')
