from pyexpat import model
from re import M
import site
from typing_extensions import Self
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
       return self.descricao

class Editora (models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()

    def __str__(self):
        return self.nome
               