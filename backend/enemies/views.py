from rest_framework import generics
from enemies.models import Dragon, Weapon, Goblin
from enemies.serializers import DragonSerializer, WeaponSerializer, GoblinSerializer

#DRAGON API
#Create dragon/ list all dragons
class DragonList(generics.ListCreateAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer
#Update, delete, or retrieve a dragon
class DragonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

#WEAPON API
class WeaponList(generics.ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class WeaponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

#GOBLIN API
class GoblinList(generics.ListCreateAPIView):
    queryset = Goblin.objects.all()
    serializer_class = GoblinSerializer

class GoblinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goblin.objects.all()
    serializer_class = GoblinSerializer