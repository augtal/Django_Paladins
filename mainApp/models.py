from os import name
from typing import SupportsAbs
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=12)

class Champion(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=CASCADE)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ChampionWinRate(models.Model):
    champion = models.ForeignKey(Champion, on_delete=CASCADE)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    winRate = models.DecimalField(max_digits=8, decimal_places=5)

class Talent(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    champion = models.ForeignKey(Champion, on_delete=CASCADE)
    
    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name