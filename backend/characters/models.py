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
    languages = models.TextField( default='')
     
"""
    user = models.ForeignKey()
    game = models.ForeignKey()
"""
 
class LoreEntry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='loreEntries')
 
class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='items')
 
class Statistics(models.Model):
    character = models.OneToOneField(Character,on_delete=models.CASCADE, null=True)

    hitPoints = models.IntegerField(default=0)
    armorClass = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    strengthModifier = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    dexterityModifier = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    constitutionModifier = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    intelligenceModifier = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    wisdomModifier = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    charismaModifier = models.IntegerField(default=0)
    fortaleza = models.IntegerField(default=0)
    reflex = models.IntegerField(default=0)
    will = models.IntegerField(default=0)
    baseAttack = models.IntegerField(default=0)
    prey = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    platinumCoins = models.IntegerField(default=0)
    goldCoins = models.IntegerField(default=0)
    silverCoins = models.IntegerField(default=0)
    copperCoins = models.IntegerField(default=0)
    lightLoad = models.IntegerField(default=0)
    mediumLoad = models.IntegerField(default=0)
    heavyLoad = models.IntegerField(default=0)
    liftOverHead = models.IntegerField(default=0)
    liftOffGround = models.IntegerField(default=0)
    pushOrDrag = models.IntegerField(default=0)
 
class Habilities(models.Model):
    character = models.OneToOneField(Character,on_delete=models.CASCADE, null=True)
    
    lockPicking = models.IntegerField(default=0)
    crafting1 = models.IntegerField(default=0)
    crafting2 = models.IntegerField(default=0)
    crafting3 = models.IntegerField(default=0)
    findOutIntention = models.IntegerField(default=0)
    sight = models.IntegerField(default=0)
    search = models.IntegerField(default=0)
    concentration = models.IntegerField(default=0)
    spellKnowledge = models.IntegerField(default=0)
    decipherScripts = models.IntegerField(default=0)
    diplomacy = models.IntegerField(default=0)
    disguise = models.IntegerField(default=0)
    deception = models.IntegerField(default=0)
    equilibrium = models.IntegerField(default=0)
    escapism = models.IntegerField(default=0)
    hide = models.IntegerField(default=0)
    listening = models.IntegerField(default=0)
    falsification = models.IntegerField(default=0)
    interpretation1 = models.IntegerField(default=0)
    interpretation2 = models.IntegerField(default=0)
    interpretation3 = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    disableMechanisms = models.IntegerField(default=0)
    trickery = models.IntegerField(default=0)
    mount = models.IntegerField(default=0)
    stealthMovement = models.IntegerField(default=0)
    swimming = models.IntegerField(default=0)
    job1 = models.IntegerField(default=0)
    job2 = models.IntegerField(default=0)
    job3 = models.IntegerField(default=0)  
    pirouette = models.IntegerField(default=0)
    gatherInformation = models.IntegerField(default=0)
    knowledge1 = models.IntegerField(default=0)
    knowledge2 = models.IntegerField(default=0)
    knowledge3 = models.IntegerField(default=0)
    jump = models.IntegerField(default=0)
    healing = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    appraise = models.IntegerField(default=0)
    animalTreatment = models.IntegerField(default=0)
    climb = models.IntegerField(default=0)
    useOfRope = models.IntegerField(default=0) 
    useOdMagicDevice = models.IntegerField(default=0)
