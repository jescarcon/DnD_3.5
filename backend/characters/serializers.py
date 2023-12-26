from rest_framework import serializers
from .models import Character, LoreEntry

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class LoreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoreEntry
        fields = '__all__'

    #We can create custom validations here
        #Object-level validation
    def validate(self, entry):
        if entry['title'] == entry['body']:
            raise serializers.ValidationError("Title and body must be different")
        return entry
        #Custom field validator, validate_<field_name>
    def validate_title(self, value):
        if value == '':
            raise serializers.ValidationError("Title must not be empty")
        return value
