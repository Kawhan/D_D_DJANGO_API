from rest_framework import serializers

from characters.models import Character

from characters.validators import Validators_characters


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            '__all__'
        )

    def validate(self, data):
        for k, v in Validators_characters.validators_data_characters.items():
            if v(data) != data:
                raise serializers.ValidationError(v(data))

        return data
