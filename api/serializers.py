from rest_framework import serializers
from api.models import Script


class ScriptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Script
        # fields = ['name', 'chosen_one', 'used', 'bat_file', 'base64_file']
        fields = ['name', 'chosen_one', 'used', 'bat_file']
