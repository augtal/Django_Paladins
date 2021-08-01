import json
from django.shortcuts import render, redirect
from pyrez.api import PaladinsAPI
from pyrez.enumerations.Format import Format

from pathlib import Path
import os
import dotenv

from .services import saveChampionCards, saveChampionTalents, saveChampions, saveChampionAbilities

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Create your views here.

def index(request):
    with PaladinsAPI(os.environ['DEV_ID'], os.environ['AUTH_KEY']) as paladins:
        # data = paladins.getChampionCards(2205)
        
        # Champion.objects.all().delete()
        
        # f = open('mainApp\APIResults\getChampions.JSON',)
        # saveChampions(data)
        # saveChampionAbilities(data)
        
        f = open('mainApp\APIResults\Error.JSON',)
        data = json.load(f)
        
        saveChampionTalents(data)
        saveChampionCards(data)
        
        #=================================================
        
        # f = open('mainApp\APIResults\ChampionIDsContinue.JSON',)
        # championIDs = json.load(f)
        
        # data = 0
        # try:
        #     for champID in championIDs:
        #         data = paladins.getChampionCards(champID['id'])
                
        #         saveChampionTalents(data)
        #         saveChampionCards(data)
        # except Exception as ex:
        #     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        #     message = template.format(type(ex).__name__, ex.args)
        #     z=0
        
        text = "this is main index"
        
        return render(request, 'mainApp/index.html', {
            'text': text,
            'champs': data
        })