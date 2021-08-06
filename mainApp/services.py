import os
from pathlib import Path
import dotenv

import json
import re

from pyrez.api import PaladinsAPI

from .models import Role, DamageType, Champion, Ability, Talent, Card

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# =================================== Database ===================================

def saveChampions(dataList):
    for data in dataList:        
        champ = Champion(
            name = data['Name'],
            role = Role.objects.get(long_name=data['Roles']),
            description = data['Lore'],
            champion_image = data['ChampionIcon_URL'],
            API_ID = data['id']
        )
        
        champ.save()

def saveChampionAbilities(dataList):
    for data in dataList:   
        for i in range(1,6):
            ability = data["Ability_" + str(i)]
            
            abil = Ability(
                championID = Champion.objects.get(API_ID=data['id']),
                name = ability['Summary'],
                description = ability['Description'],
                damageType = DamageType.objects.get(slug_name=ability['damageType']), 
                ability_image = ability['URL']
            )
            
            abil.save()

def saveChampionTalents(cardDataList):
    for data in cardDataList:
        if data['rarity'].lower() == "legendary":
            talentDescription = data['card_description']
            reg = re.split('\[(.+)\] ', talentDescription)
            
            championAPIID = Champion.objects.get(API_ID=data['champion_id'])
            
            if len(reg) <= 1:
                tal = Talent(
                    championID = championAPIID,
                    name = data['card_name'],
                    type = 0,
                    description = reg[len(reg)-1],
                    talent_image = data['championTalent_URL']
                )
                
                print("Row in Talent table needs checking API_ID: " + str(championAPIID.API_ID) + " talent name: " + data['card_name'] + " | check: type")
            #normal progression
            else:
                tal = Talent(
                    championID = championAPIID,
                    name = data['card_name'],
                    type = reg[len(reg)-2],
                    description = reg[len(reg)-1],
                    talent_image = data['championTalent_URL']
                )
            
            tal.save()

def saveChampionCards(cardDataList):
    for data in cardDataList:
        if data['rarity'].lower() == "common":
            talentDescription = data['card_description']
            reg = re.split('\[(.+)\] ', talentDescription)
            
            pattern = '\{scale=\s?([-+]?[0-9]+[.,]?[0-9]*)\|([-+]?[0-9]+[.,]?[0-9]*).?\}'
            
            if len(reg) <= 1:
                desReg = re.split(pattern, reg[0])
                regType = 0
            # normal progression
            else:
                desReg = re.split(pattern, reg[2])
                regType = reg[len(reg)-2]
            
            
            championAPIID = Champion.objects.get(API_ID=data['champion_id'])
            
            # for one scale in description
            # normal progression
            if len(desReg) == 4:
                card = Card(
                    championID = championAPIID,
                    name = data['card_name'],
                    description = desReg[0] + "|" + desReg[1] + "|" + desReg[3],
                    type = regType,
                    base1 = desReg[1],
                    base2 = 0,
                    increase1 = desReg[2],
                    increase2 = 0,
                    card_image = data['championCard_URL'],
                )
            
            # for none scale in description
            elif len(desReg) < 2:
                card = Card(
                    championID = championAPIID,
                    name = data['card_name'],
                    description = desReg[0],
                    type = regType,
                    base1 = 0,
                    base2 = 0,
                    increase1 = 0,
                    increase2 = 0,
                    card_image = data['championCard_URL'],
                )
                
                print("Row in Card table needs checking API_ID: " + str(championAPIID.API_ID) + " card name: " + data['card_name'] + " | check: type, base1, increase1")
            
            # for two scales in description
            elif len(desReg) == 7:
                card = Card(
                    championID = championAPIID,
                    name = data['card_name'],
                    description = desReg[0] + "|" + desReg[1] + "|" + desReg[3] + "|" + desReg[4] + "|" + desReg[6],
                    type = regType,
                    base1 = desReg[1],
                    base2 = desReg[1+3],
                    increase1 = desReg[2],
                    increase2 = desReg[2+3],
                    card_image = data['championCard_URL'],
                )
                
                print("Row in Card table needs checking API_ID: " + str(championAPIID.API_ID) + " card name: " + data['card_name'] + " | check: type, base1, base2, increase1, increase2 | it should have 2 scales")
            
            card.save()

def insertToDatabase():
    with PaladinsAPI(os.environ['DEV_ID'], os.environ['AUTH_KEY']) as paladins:
        
        print(paladins.getDataUsed())
        data = paladins.getChampionCards(2073)
        z=0
        
        
        return (data,"empty")
        
        #================= Champions and abilities ===================
        
        # f = open('mainApp\APIResults\getChampions.JSON',)
        # data = json.load(f)
        # saveChampions(data)
        # saveChampionAbilities(data)
        
        #================= Error checking ===================
        
        # f = open('mainApp\APIResults\Error.JSON',)
        # data = json.load(f)
        
        # saveChampionTalents(data)
        # saveChampionCards(data)
        
        #=================================================
        
        #================= All cards/talents ===================
        
        # f = open('mainApp\APIResults\ChampionIDs.JSON',)
        # championIDs = json.load(f)
    
        # try:
        #     for champion in championIDs:
        #         champID = champion['id']
        #         data = paladins.getChampionCards(champID)
                
        #         saveChampionTalents(data)
        #         saveChampionCards(data)
        # except Exception as ex:
        #     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        #     message = template.format(type(ex).__name__, ex.args)
        #     return (data, message)
        
        #================= All cards/talents END ===================
    
# =================================== Database END ===================================
