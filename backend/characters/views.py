from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Character
class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetails(generics.RetrieveDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

#Lore Entry
class LoreEntryList(generics.ListCreateAPIView):    
    queryset = LoreEntry.objects.all()
    serializer_class = LoreEntrySerializer

class LoreEntryDetails(generics.RetrieveDestroyAPIView):    
    queryset = LoreEntry.objects.all()
    serializer_class = LoreEntrySerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

class StatisticsList(generics.ListCreateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class StatisticsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class HabilitiesList(generics.ListCreateAPIView):
    queryset = Habilities.objects.all()
    serializer_class = HabilitiesSerializer

class HabilitiesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habilities.objects.all()
    serializer_class = HabilitiesSerializer
