from django.db import models
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=12)
    long_name = models.CharField(max_length=21)
    
    def __str__(self):
        return self.name
    
class DamageType(models.Model):
    name = models.CharField(max_length=10)
    slug_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Champion(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=CASCADE)
    description = models.CharField(max_length=900)
    champion_image = models.URLField(null=True)
    API_ID = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Ability(models.Model):
    championID = models.ForeignKey(Champion, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    damageType = models.ForeignKey(DamageType, on_delete=CASCADE)
    ability_image = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class Talent(models.Model):
    championID = models.ForeignKey(Champion, on_delete=CASCADE)
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=75)
    description = models.CharField(max_length=800)
    talent_image = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class Card(models.Model):
    championID = models.ForeignKey(Champion, on_delete=CASCADE)
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=800)
    type = models.CharField(max_length=75)
    base1 = models.DecimalField(max_digits=8, decimal_places=3)
    base2 = models.DecimalField(max_digits=8, decimal_places=3)
    increase1 = models.DecimalField(max_digits=8, decimal_places=3)
    increase2 = models.DecimalField(max_digits=8, decimal_places=3)
    card_image = models.URLField(null=True)
    
    def __str__(self):
        return self.name

class ChampionWinRate(models.Model):
    championID = models.ForeignKey(Champion, on_delete=CASCADE)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    winRate = models.DecimalField(max_digits=8, decimal_places=5)
    updated_at = models.DateTimeField()