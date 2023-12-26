from django.db import models

class Dragon(models.Model):
    #Enums in django are declared this way
    class Element(models.TextChoices):
        #  Actual value, human readable name
        WATER = 'WATER', 'Water'
        FIRE = 'FIRE', 'Fire'
        EARTH = 'EARTH', 'Earth'
        WIND = 'WIND', 'Wind'
        LIGHT = 'LIGHT', 'Light'
        DARK = 'DARK', 'Dark'

    dragon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    element = models.CharField(max_length=10, choices = Element.choices)
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    speed = models.IntegerField()
    critical_rate = models.FloatField()
    critical_damage = models.IntegerField()

class Weapon(models.Model):
    class WeaponType(models.TextChoices):
        SWORD = 'SWORD', 'Sword'
        BOW = 'BOW', 'Bow'
        STAFF = 'STAFF', 'Staff'
        AXE = 'AXE', 'Axe'
        HAMMER = 'HAMMER', 'Hammer'
        SPEAR = 'SPEAR', 'Spear'

    id_weapon = models.AutoField(primary_key=True)
    range = models.IntegerField()
    damage  = models.IntegerField()
    weapon_type = models.CharField(max_length=10, choices = WeaponType.choices)


class Goblin(models.Model):
    id_goblin = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    speed = models.IntegerField()

    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='goblins')
    