from rest_framework import serializers
from .models import Doubts

class DoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doubts
        fields='__all__'