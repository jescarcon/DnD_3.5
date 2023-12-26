from django.db import models

class Character(models.Model):
    class Alignment(models.TextChoices):
        LEGAL_GOOD = 'LEGAL_GOOD', 'Legal Good'
        LEGAL_NEUTRAL = 'LEGAL_NEUTRAL', 'Legal Neutral'
        LEGAL_EVIL = 'LEGAL_EVIL', 'Legal Evil'
        NEUTRAL_NEUTRAL = 'NEUTRAL_NEUTRAL', 'Neutral Neutral' 
        NEUTRAL_GOOD = 'NEUTRAL_GOOD', 'Neutral Good'
        NEUTRAL_EVIL = 'NEUTRAL_EVIL', 'Neutral Evil'
        CHAOTIC_GOOD = 'CHAOTIC_GOOD', 'Chaotic Good'
        CHAOTIC_NEUTRAL = 'CHAOTIC_NEUTRAL', 'Chaotic Neutral'
        CHAOTIC_EVIL = 'CHAOTIC_EVIL', 'Chaotic Evil'
    
    class CharacterClass(models.TextChoices):
        MAGE = 'MAGE', 'Mage'
        EXPLORER = 'EXPLORER', 'Explorer'
        WARRIOR = 'WARRIOR', 'Warrior'
        CLERIC = 'CLERIC', 'Cleric'
        PALADIN = 'PALADIN', 'Paladin'
        BARBARIAN = 'BARBARIAN', 'Barbarian'
        ROGUE = 'ROGUE', 'Rogue'
        SORCERER = 'SORCERER', 'Sorcerer'
        DRUID = 'DRUID', 'Druid'
        MONK = 'MONK', 'Monk'
        BARD = 'BARD', 'Bard'
        WARLOCK = 'WARLOCK', 'Warlock'

    name = models.CharField(max_length=50)
    isNPC = models.BooleanField(default=False)
    level = models.IntegerField(default=1)
    race = models.CharField(max_length=50)
    image = models.ImageField(upload_to='characters/images/', default='characters/default.png')
    alignment = models.CharField(max_length=50, choices=Alignment.choices)
    characterClass = models.CharField(max_length=50, choices=CharacterClass.choices)

    '''
    user = models.ForeignKey()
    game = models.ForeignKey()
    '''

class LoreEntry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='loreEntries')

