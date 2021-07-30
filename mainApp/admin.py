from django.contrib import admin
from .models import Champion, Talent, Card

# Register your models here.

admin.site.register(Champion)
admin.site.register(Talent)
admin.site.register(Card)