from django.contrib import admin
from .models import Champion, Talent, Card, Role, DamageType, Ability

# Register your models here.

admin.site.register(Champion)
admin.site.register(Talent)
admin.site.register(Card)
admin.site.register(Role)
admin.site.register(DamageType)
admin.site.register(Ability)