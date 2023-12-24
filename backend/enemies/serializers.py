from rest_framework import serializers
from .models import Dragon, Weapon, Goblin

#Serializers handle converting data to and from JSON

class DragonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = '__all__'

class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['weapon_type']

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'

class GoblinSerializer(serializers.ModelSerializer):
    weapon = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Weapon.objects.all(),
        slug_field='weapon_type'
    )

    class Meta:
        model = Goblin
        fields = ['id_goblin', 'name', 'attack', 'defense', 'hp', 'speed', 'weapon']