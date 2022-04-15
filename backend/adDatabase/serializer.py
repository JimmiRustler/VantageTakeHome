from rest_framework import serializers
from .models import ad

class adSerializer(serializers.ModelSerializer):
    class Meta:
        model = ad
        fields = ('image', 'URL', 'adInfo', 'adTitle')