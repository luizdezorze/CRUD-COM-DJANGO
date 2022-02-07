from django.db import models


class Tratamentos(models.Model):
    paciente = models.CharField(max_length=150)
    rh = models.CharField(max_length=150)
    setor = models.CharField(max_length=150)
    medicamento = models.CharField(max_length=150)
    dose = models.IntegerField()
    unidade = models.CharField(max_length=150)
    frequencia = models.IntegerField()
    duracao = models.IntegerField()
