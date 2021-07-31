import json
from django.shortcuts import render, redirect
from pyrez.api import PaladinsAPI
from pyrez.enumerations.Format import Format

from pathlib import Path
import os
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Create your views here.

def index(request):
    with PaladinsAPI(os.environ['DEV_ID'], os.environ['AUTH_KEY']) as paladins:
        data = paladins.getChampionCards(2205)
        
        # champs = paladins.getGods()
        
        text = "this is main index"
        
        return render(request, 'mainApp/index.html', {
            'text': text,
            'champs': data
        })