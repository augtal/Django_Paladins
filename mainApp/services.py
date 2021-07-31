from .models import Role, DamageType, Champion, Ability

def saveChampions(dataList):
    for data in dataList:        
        champ = Champion(
            name = data['Name'],
            role = Role.objects.get(long_name=data['Roles']),
            description = data['Lore'],
            champion_image = data['ChampionIcon_URL']
        )
        
        champ.save()

def saveChampionAbilities(dataList):
    for data in dataList:   
        for i in range(1,6):
            ability = data["Ability_" + str(i)]
            
            abil = Ability(
                championID = Champion.objects.get(name=data['Name']),
                name = ability['Summary'],
                description = ability['Description'],
                damageType = DamageType.objects.get(slug_name=ability['damageType']), 
                ability_image = ability['URL']
            )
            
            abil.save()
