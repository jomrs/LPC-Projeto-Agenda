from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name="Nome", max_length=60, blank=True, null=True)
    data_nacimento = models.DateField("Data de Nascimento")
    telefone = models.CharField(verbose_name="Telefone", max_length=14)
    email = models.EmailField("Email", max_length=254)

    def __str__(self):
        return self.nome

class TipoAgenda(models.Model):
    nome = models.CharField(verbose_name="Tipo de Agenda", max_length=8)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField(verbose_name="Compromisso", max_length=256)
    descricao = models.CharField(verbose_name="Descrição", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    nome = models.CharField(verbose_name="Evento", max_length=256, blank=True, null=True)
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField("Data", blank=True, null=True)
    tipo = models.ForeignKey(TipoAgenda, on_delete=models.CASCADE)
    compromissos = models.ManyToManyField(Compromisso)

    def __str__(self):
        return self.nome

