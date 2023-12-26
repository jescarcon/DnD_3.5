from django.shortcuts import render
from rest_framework import generics
from .models import Character, LoreEntry
from .serializers import CharacterSerializer, LoreEntrySerializer

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


