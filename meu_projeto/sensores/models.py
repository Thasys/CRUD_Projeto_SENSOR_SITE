import uuid
from django.db import models

class Sensor(models.Model):
    sensor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Leitura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperatura = models.FloatField()
    umidade = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leitura de {self.sensor.nome} em {self.data_hora}"
